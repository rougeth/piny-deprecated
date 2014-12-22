from string import digits, ascii_letters


class BaseConverter(object):

    def converter(self, number, frombase, tobase):
        # Based on http://code.activestate.com/recipes/111286/
        if str(number)[0] == '-':
            number = str(number)[1:]
            neg = 1
        else:
            neg = 0

        # make an integer out of the number
        x = 0
        for digit in str(number):
            x = x * len(frombase) + frombase.index(digit)

        # create the result in base 'len(tobase)'
        if x == 0:
            res = tobase[0]
        else:
            res = ""
            while x > 0:
                digit = x % len(tobase)
                res = tobase[digit] + res
                x = int(x / len(tobase))
            if neg:
                res = '-' + res
        return res


class Base62(BaseConverter):

    base10 = digits
    base62 = digits + ascii_letters

    def from_decinal(self, number):
        return self.converter(number, self.base10, self.base62)

    def to_decinal(self, number):
        return self.converter(number, self.base62, self.base10)
