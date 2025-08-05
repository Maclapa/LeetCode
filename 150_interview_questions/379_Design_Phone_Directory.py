#Design a Phone Directory which supports the following operations:
# get: Provide a number which is not assigned to anyone.
# check: Check if a number is available or not.
# release: Recycle or release a number.
# Example:
#
# // Init a phone directory containing a total of 3 numbers: 0, 1, and 2.
# PhoneDirectory directory = new PhoneDirectory(3);
#
# // It can return any available phone number. Here we assume it returns 0.
# directory.get();
#
# // Assume it returns 1.
# directory.get();
#
# // The number 2 is available, so return true.
# directory.check(2);
#
# // It returns 2, the only number that is left.
# directory.get();
#
# // The number 2 is no longer available, so return false.
# directory.check(2);
#
# // Release number 2 back to the pool.
# directory.release(2);
#
# // Number 2 is available again, return true.
# directory.check(2);


class PhoneDir():
    def __init__(self, max_number):
        self.max_number = max_number
        self.numbers = [i for i in range(1,max_number+1)]

    def get(self):
        value_to_return = self.numbers[0]
        self.numbers = self.numbers[1:]
        return value_to_return

    def check(self, value):
        return value in self.numbers

    def release(self, value):
        if value not in self.numbers:
            self.numbers.append(value)


phone = PhoneDir(3)
print(phone.get())
print(phone.release(1))
print(phone.check(1))