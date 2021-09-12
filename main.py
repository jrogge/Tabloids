import tab_3 as t3
import tab_4 as t4
from Tabloid import merge_sort

# tabloids on [3]
srtd_3 = merge_sort(t3.tabs, [])
# merge sort results in increasing order, to display as hasse diagram reverse
for tab in srtd_3[::-1]:
    print(tab)

print("================")
print()
print("================")

# tabloids on [4]
srtd_4 = merge_sort(t4.tabs, [])
# merge sort results in increasing order, to display as hasse diagram reverse
for tab in srtd_4[::-1]:
    print(tab)
