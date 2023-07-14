# This sample tests that unhashable user classes are detected as unhashable.

class A:
    ...

s1 = {A()}
d1 = {A(): 100}

class B:
    def __eq__(self, other):
        ...

# Both of these should generate an error because a class that
# defines __eq__ but not __hash__ is not hashable
s2 = {B()}
d2 = {B(): 100}

class C:
    __hash__: None = None # type: None

class D(B, C):
    ...

# Both of these should generate an error because B is unhashable.
s3 = {UnhashableSub()}
d3 = {UnhashableSub(): 100}

class E:
    def __hash__(self):
        ...

class F(D, E):
    ...

# Both of these should generate an error because D is unhashable.
s4 = {F()}
d4 = {F(): 100}

class G(E, D):
    ...

# Both of these should NOT generate an error because E defines __hash__.
s5 = {G()}
d5 = {G(): 100}