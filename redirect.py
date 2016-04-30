# This script creates redirect links from codalab.org to worksheets.codalab.org and competitions.codalab.org.

import os

# Create redirect links

# cl wls tag=paper -u
worksheets = """
0x7f9151ec074f4f589e4d4786db7bb6de
0xc6edf0c9bec643ac9e74418bd6ad4136
0x66df55eda5054cbf9e173520c7b6ac3d
0x106abb3b47be492aa7387f528c943faa
0x8967960a7c644492974871ee60198401
0x269ef752f8c344a28383240f7bb2be9c
0xf26cd79d4d734287868923ad1067cf4c
0x56dc93bcd3a647b197ad6e4b9d56f336
0xfcace41fdeec45f3bc6ddf31107b829f
0xba659fe363cb46e7a505c5b6a774dc8a
0xc9db508bb80446d2b66cbc8e2c74c052
"""

# wget -q --no-check-certificate https://competitions.see4c.eu/competitions -O - | grep competitionID.*value
competitions = """
6991
6981
6971
6961
6351
6121
5191
5181
4081
4711
3791
4971
5941
3221
2611
2321
2241
2231
1661
1471
1381
1311
991
981
971
1
191
"""

forums = """
3731
"""

def create_redirect(items, base_path, host):
    for item in items.split('\n'):
        if not item: continue
        print os.path.join(host, base_path, item)
        os.system('mkdir -p ' + os.path.join(base_path, item))
        web_path = host if '/' in host else os.path.join(host, base_path, item)
        with open(os.path.join(base_path, item, 'index.html'), 'w') as f:
            print >>f, '<meta http-equiv="refresh" content="0; url=https://%s">' % web_path

create_redirect('worksheets', '', 'worksheets.see4c.eu')
create_redirect(worksheets, 'worksheets', 'worksheets.see4c.eu')

create_redirect('competitions', 'competitions', 'competitions.see4c.eu')
create_redirect('AutoML', '', 'competitions.see4c.eu/competitions/2321')
create_redirect('automl', '', 'competitions.see4c.eu/competitions/2321')
create_redirect(competitions, 'competitions', 'competitions.see4c.eu')
create_redirect(forums, 'forums', 'competitions.see4c.eu')
