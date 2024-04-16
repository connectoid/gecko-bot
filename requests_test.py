import random
from time import sleep

from services.requests_insta import get_video_requests

urls = [
    'https://www.instagram.com/reel/C5lwbPYIzMs/?igsh=MTNiNml5bGV2aXk3ZA==',
    'https://www.instagram.com/reel/C4WiPb3vNX3/?igsh=N2ZsdXhob25vbmh6',
    'https://www.instagram.com/reel/C5Gy7-ANVKy/?igsh=MTRxNDV6b21hdWU4Yw==',
    'https://www.instagram.com/reel/C3PjaTXseE8/?igsh=MXJ2c2s4b2x2am1nYQ==',
    'https://www.instagram.com/reel/C23dhF3PtDR/?igsh=MWp2MHJzMDA5dmxvOA==',
    'https://www.instagram.com/reel/C4iOAtroTD6/?igsh=MTlhM2FmYjFja2R4bQ==',
    'https://www.instagram.com/reel/C5nNnLuMNxN/?igsh=MXNkN2lxMTFmZzJs',
    'https://www.instagram.com/reel/C3KzmC7vY38/?igsh=cTRuMjFwY2lkdDMz',
    'https://www.instagram.com/reel/C4TQ_dso068/?igsh=NjZ5YWU2Mnh1cWZs',
    'https://www.instagram.com/reel/C5n47AcRZDf/?igsh=a3JqNmdybzRwZW9n',
    'https://www.instagram.com/reel/C4pOp6LoWOA/?igsh=MTU0NnIzNWdpdGVwZg==',
    'https://www.instagram.com/reel/C5tbAv_I9uR/?igsh=MTZoZmdndnZxZWJ0bQ==',
    'https://www.instagram.com/reel/C2Sb310oe5q/?igsh=azRlYWd1MnZ0dXRt',
    'https://www.instagram.com/reel/C5PLxkfPnBM/?igsh=dDVwaGx3OTZoMXdz',
    'https://www.instagram.com/reel/C5QhP1qulXE/?igsh=MXcxZG56bmM0YnB5Zw==',
    'https://www.instagram.com/reel/C5l4dWzrGD0/?igsh=MTd2MTczYzExYWgwMA==',
    'https://www.instagram.com/reel/C5vSVt_L6pA/?igsh=Y3Frcno2aTM5cG5u',
    'https://www.instagram.com/reel/C5vSVt_L6pA/?igsh=Y3Frcno2aTM5cG5u',
    'https://www.instagram.com/reel/C3HdUU-t_Bb/?igsh=ZW9mMXNoYzN5dDk0',
    'https://www.instagram.com/reel/C5G-hC8P1M4/?igsh=MTB6NmR2MXFhZ2t1YQ==',
    'https://www.instagram.com/reel/C4D0pIJtqWI/?igsh=MWJ3bWJqajlyOXZrZg==',
    'https://www.instagram.com/reel/C20P8tTOri2/?igsh=Z3RzYmFmM2g1aDh3',
    'https://www.instagram.com/reel/C5h1wPQCKeK/?igsh=YTV1Z3Q3a2d5anhk',
    'https://www.instagram.com/reel/C5uVe3FpVU7/?igsh=aGh3OGhmeDQzaHN3',
    'https://www.instagram.com/reel/C5i0yN5trnu/?igsh=MTgzcHEwbHVsNnZtag==',
    'https://www.instagram.com/reel/C45nBIZy22e/?igsh=aDBkNGs1c2c1NGN4',
    'https://www.instagram.com/reel/C4_fCNGvwVW/?igsh=MThjazRmYml4OHdyeQ==',
    'https://www.instagram.com/reel/C2mBk0qLTqR/?igsh=dzFjM2llMGJ6MGkz',
    'https://www.instagram.com/reel/C2xq_V0s8Di/?igsh=MWp0dGJpa3I4dDExbw==',
    'https://www.instagram.com/reel/C4ylFifITPV/?igsh=MW9janoxMWc3c3FxbQ==',
    'https://www.instagram.com/reel/C4RsCB5p87L/?igsh=MTkyZHJub2kwZWo3dg==',
    'https://www.instagram.com/reel/C2c1FU-rDN_/?igsh=cmN5d3BneHhnN3Bx',
    'https://www.instagram.com/reel/C5RdS4Zv11r/?igsh=MTh2YTNnaTZ5eWJnNw==',
    'https://www.instagram.com/reel/C4-QjdlxsrZ/?igsh=a3N5ZjR6b3Rnem40',
    'https://www.instagram.com/reel/C5dfNWFsHME/?igsh=MTh3YTI3OHc3MXU1Yg==',
    'https://www.instagram.com/reel/C4gIsYXIENE/?igsh=M2Nva2UxaGg3bG95',
    'https://www.instagram.com/reel/C3m-GW6sa8I/?igsh=MXZoaWZpNG41czdseQ==',
    'https://www.instagram.com/reel/C4eXD-AJJkn/?igsh=bXJ0MW5sY3NyN3J3',
    'https://www.instagram.com/reel/C4icygCMoXM/?igsh=MTJxbmZ6ZDFycDdzZw==',
    'https://www.instagram.com/reel/C4ibU3mI43U/?igsh=MWlsaW9sdWp3YWhiZg==',
    'https://www.instagram.com/reel/C5W-ESlI3MZ/?igsh=YnUyZTJpNjRoczJj',
    'https://www.instagram.com/reel/C2QNGCAopKO/?igsh=MWw2NjU2NjB4a3pvcA==',
    'https://www.instagram.com/reel/C5SXjgOsb7j/?igsh=ZnR6dG5jbTUwYnU0',
    'https://www.instagram.com/reel/C2XaLbJoDkk/?igsh=MTMxNGMyNDJuMnZqYQ==',
    'https://www.instagram.com/reel/C4v-AaNNIIj/?igsh=a244aXJhOWNybTZh',
    'https://www.instagram.com/reel/C3nKe6atvkQ/?igsh=MWprNmpkM250a3U5eg==',
    'https://www.instagram.com/reel/C5WJIEAqOg3/?igsh=dnd1cG96MmNpbW55',
    'https://www.instagram.com/reel/C5g9gSTAfXb/?igsh=eG9rNGY0aWo3cTR2',
    'https://www.instagram.com/reel/C5TT1mOrrT-/?igsh=N3c2bmc5OW5tczRs',
    'https://www.instagram.com/reel/C20ur76ydSH/?igsh=MXRzdDZ0dGExNTdjZw==',
    'https://www.instagram.com/reel/C5bVvZMtvbf/?igsh=MW5kanAwM3QxZXE2dA==',
    'https://www.instagram.com/reel/C5vXafiK753/?igsh=MzR1Z3kyOTYyeDJ5',
    'https://www.instagram.com/reel/C5S1k4yozK9/?igsh=MTJlYnFqdzB5NnQ4MQ==',
    'https://www.instagram.com/reel/C2kY4_XtoC-/?igsh=YWIzdXF0dXZpY2Fv',
    'https://www.instagram.com/reel/C4y1PMhv3hB/?igsh=MTBsc2JtZnZ4MHJ4Yw==',
    'https://www.instagram.com/reel/C35R-hmNCDy/?igsh=MWlsN2VwZXhxbmlzZw==',
    'https://www.instagram.com/reel/C2hjGRLMSuF/?igsh=MTdvYnNseHV6Y2s4Zw==',
    'https://www.instagram.com/reel/C5CaZ_DyF3W/?igsh=MWxvZnRyYjhwZjJnZA==',
    'https://www.instagram.com/reel/C40QgjSLn7m/?igsh=emQyNHJpNGtyYnhz',
    'https://www.instagram.com/reel/C4q3da9LjVS/?igsh=emtobWdwZzN2cGF1',
    'https://www.instagram.com/reel/C4-0liRMD0B/?igsh=N3c4Nzg5amx5bXRr',
]
success_count = fail_count = 0
for count in range(1, 101):
    url = random.choice(urls)
    shortcode = url.split('/reel/')[1].split('/')[0]
    interval = random.randint(1, 2)
    video_url = get_video_requests(shortcode)
    if video_url:
        print(f'{count}. Ссылка {video_url[:20]} получена удачно. Ждем {interval} сек.')
        sleep(interval)
        success_count += 1
    else:
        print(f'{count}. Ссылка не получена. Ждем {interval} сек.')
        sleep(interval)
        fail_count += 1

print(f'Удачных: {success_count} Неудачных: {fail_count}')
