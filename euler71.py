from fractions import gcd

def closest_num(target_denom, start_at=1):
                
        lown = start_at
        lowd = target_denom
        while lown * 7 < lowd * 3:
                lown += 1
        return lown -1
   

                
last_closest = closest_num(3)
closestn = last_closest
closestd = 3
for i in range(1000000):
        last_closest = closest_num(i, start_at=last_closest)
        if closestn * i < last_closest * closestd:
                closestn = last_closest
                closestd = i

print closestn/gcd(closestn,closestd)
print closestd/gcd(closestn,closestd)


