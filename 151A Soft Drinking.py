n,k,l,c,d,p,nl,np=map(int,input().split())
total_drink = k * l
total_slices = c * d
toasts_by_drink = total_drink // nl
toasts_by_lime = total_slices
toasts_by_salt = p // np
max_total_toasts = min(toasts_by_drink, toasts_by_lime, toasts_by_salt)
print(max_total_toasts // n)