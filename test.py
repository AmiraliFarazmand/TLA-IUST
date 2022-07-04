import re
from time import pthread_getcpuclockid

st = '<B>sdadad<ss>sd<A>'
st=st.replace('<B>' , '' )
gt = re.findall( r'^<..' , st )
gtm = re.findall( '^<[a-zA-Z].+>$' , st )
gtn = re.findall( r'<[A-Za-z]*>' , st )
print(gt)
print(gtm)
print(gtn)
print(st)
