print("Lungimea gardului lotului patrat este de 48 metri")
perim_pat = 48
lat_pat = perim_pat // 4
lat_dr = 9
aria_pat = lat_pat ** 2
lun_dr = aria_pat // lat_dr
perim_dr = (2 * lun_dr) + (2 * lat_dr)
print("Lungimea gardului lotului dreptunghic este de",perim_dr,"metri")