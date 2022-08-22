import random

icecekler = ["kahve",
            "muzlu-sut",
            "cappucione",
            "filtre-kahve"]

yiyecekler = ["pasta",
              "borek",
              "corek",
              "kruvasan",
              ]

random_icecekler = random.choice(icecekler)
random_yiyecekler = random.choice(yiyecekler)
random_yiyecekler_2 = random.choice(yiyecekler)

if random_yiyecekler == random_yiyecekler_2:
    random_yiyecekler_2 = random.choice(yiyecekler)

print(f"Bugunku icecegimiz {random_icecekler} yaninda {random_yiyecekler} ve {random_yiyecekler_2}")

