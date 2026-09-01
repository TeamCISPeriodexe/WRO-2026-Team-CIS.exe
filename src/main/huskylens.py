import struct
from time import sleep_ms
from hub import port

class Block:
    __slots__ = ('x', 'y', 'width', 'height', 'ID')
    def __init__(self, x, y, w, h, ID):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.ID = ID

class HuskyLens:
    H1 = b'\x55\xaa\x11'
    V2H = b'\x55\xaa'
    V1_REQ = 0x20
    V1_ALG = 0x2D
    V1_KNOCK = 0x2C
    V1_INFO = 0x29
    V1_BLOCK = 0x2A
    V1_OK = 0x2E
    V2_KNOCK = 0x00
    V2_RESULT = 0x01
    V2_ALG = 0x0A
    V2_OK = 0x1A
    V2_INFO = 0x1B
    V2_BLOCK = 0x1C

    def __init__(self, name='E', baud=9600):
        self.uart = getattr(port, name)
        self.uart.mode(1)
        sleep_ms(300)
        self.uart.baud(baud)
        self.uart.pwm(100)
        sleep_ms(2200)
        try:
            self.uart.read(64)
        except:
            pass
        self.version = None
        self._detect()

    def _sum(self, d):
        s = 0
        for b in d:
            s = (s + b) & 255
        return s

    def _avail(self):
        try:
            return self.uart.waiting()
        except:
            try:
                return self.uart.any()
            except:
                return True

    def _readn(self, n):
        o = bytearray()
        loops = 0
        while len(o) < n and loops < 700:
            if self._avail():
                b = self.uart.read(1)
                if b:
                    o.extend(b)
            else:
                sleep_ms(1)
            loops += 1
        return bytes(o)

    def _write(self, d):
        self.uart.write(d)
        sleep_ms(5)

    def _flush(self):
        for _ in range(5):
            if self._avail():
                try:
                    self.uart.read(64)
                except:
                    pass
            else:
                break

    def _cmd1(self, c, p=b''):
        n = len(p)
        m = bytearray(6 + n)
        m[0:3] = self.H1
        m[3] = n
        m[4] = c
        if n:
            m[5:5+n] = p
        m[5+n] = self._sum(m[:5+n])
        self._write(bytes(m))

    def _read1(self):
        for _ in range(80):
            if self._readn(3) == self.H1:
                break
        else:
            return None, None
        z = self._readn(2)
        if len(z) < 2:
            return None, None
        n = z[0]
        c = z[1]
        p = self._readn(n)
        q = self._readn(1)
        if len(q) != 1:
            return None, None
        chk = bytearray(self.H1)
        chk.append(n)
        chk.append(c)
        chk.extend(p)
        if q[0] == self._sum(chk):
            return c, p
        return None, None

    def _cmd2(self, c, a=0, p=b''):
        n = len(p)
        m = bytearray(6 + n)
        m[0] = 0x55
        m[1] = 0xAA
        m[2] = c
        m[3] = a
        m[4] = n
        if n:
            m[5:5+n] = p
        m[5+n] = self._sum(m[:5+n])
        self._write(bytes(m))

    def _read2(self):
        h = self._readn(5)
        if len(h) != 5 or h[0] != 0x55 or h[1] != 0xAA:
            return None
        p = self._readn(h[4] + 1)
        if len(p) != h[4] + 1:
            return None
        return h + p

    def knock(self):
        if self.version == 1:
            self._cmd1(self.V1_KNOCK)
            for _ in range(6):
                c, _ = self._read1()
                if c == self.V1_OK:
                    return True
                sleep_ms(10)
            return False
        self._cmd2(self.V2_KNOCK)
        for _ in range(4):
            p = self._read2()
            if p is not None and len(p) >= 3 and p[2] == self.V2_OK:
                return True
            sleep_ms(50)
        return False

    def _detect(self):
        self.version = 2
        if self.knock():
            print("HUSKY V2")
            return
        self.version = 1
        if self.knock():
            print("HUSKY V1")
            return
        self.version = None

    def mode_object_recognition(self):
        if self.version == 1:
            self._cmd1(self.V1_ALG, struct.pack("h", 4))
        elif self.version == 2:
            p = bytearray([4, 0])
            p.extend(struct.pack("<hhhh", 0, 0, 0, 0))
            self._cmd2(self.V2_ALG, 0, bytes(p))
        else:
            return False
        return self.knock()

    def get_blocks(self):
        r = []
        if self.version == 1:
            self._cmd1(self.V1_REQ)
            c, p = self._read1()
            if c != self.V1_INFO or len(p) < 2:
                return r
            n = struct.unpack("h", p[:2])[0]
            for _ in range(n):
                c, d = self._read1()
                if c == self.V1_BLOCK and len(d) >= 10:
                    x, y, w, h, i = struct.unpack("hhhhh", d[:10])
                    r.append(Block(x, y, w, h, i))
            return r

        if self.version == 2:
            self._cmd2(self.V2_RESULT, 2)
            sleep_ms(50)
            p = self._read2()
            if p is None or len(p) < 9 or p[2] != self.V2_INFO:
                return r
            n = struct.unpack("<h", bytes(p[7:9]))[0]
            for _ in range(n):
                sleep_ms(10)
                q = self._read2()
                if q is not None and len(q) >= 15 and q[2] == self.V2_BLOCK:
                    i = struct.unpack("b", bytes(q[5:6]))[0]
                    x, y, w, h = struct.unpack("<hhhh", bytes(q[7:15]))
                    r.append(Block(x, y, w, h, i))
            self._flush()
        return r

def find_obstacle(husky, green_id=1, red_id=2, swap_logic=False):
    blocks = husky.get_blocks()
    candidates = []

    if swap_logic:
        dir_green = "RIGHT"
        dir_red = "LEFT"
    else:
        dir_green = "LEFT"
        dir_red = "RIGHT"

    for b in blocks:
        if b.ID == green_id:
            candidates.append((dir_green, b))
        elif b.ID == red_id:
            candidates.append((dir_red, b))

    if not candidates:
        return None, None

    candidates.sort(key=lambda item: item[1].width * item[1].height, reverse=True)
    return candidates[0]