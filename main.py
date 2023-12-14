from diaries.DiarySample import DiarySample
from diaries.UtitaneDiary import UtitaneDiary
from diaries.NagataniDiary import NagataniDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(), 
    UtitaneDiary(),
    NagataniDiary(),
]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()