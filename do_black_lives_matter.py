#!/usr/bin/env python
"""Do black lives matter?"""


class Life:
    __matters = True

    @property
    def matters(self):
        return self.__matters


class Person:
    def __init__(self, skin_color):
        self.skin_color = skin_color
        self.life = Life()


if __name__ == "__main__":
    people = []
    black_people = []
    for n in range(100):
        if n % 2 == 0:
            p = Person(skin_color="black")
            black_people.append(p)
        else:
            p = Person(skin_color="white")
        people.append(p)

    all_lives_matter = all([person.life.matters for person in people])
    black_lives_matter = all([person.life.matters for person in black_people])

    # No real reason to assert this because it's not really what we're asking,
    # but we'll do it anyway (silently)
    assert all_lives_matter

    # Check some logic here just in case
    if black_lives_matter and not all_lives_matter:
        raise SystemError

    # Okay, if we've made it here, it's a good sign
    # Now let's answer the question at hand
    if black_lives_matter:
        print("Yes")
    else:
        print("No")
