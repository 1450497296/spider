import  requests
from selenium import webdriver
from lxml import html
from lxml.html import fromstring, tostring
etree = html.etree

s=0
start_page=int(input('输入起始页码：'))
end_page=int(input('输入结束页码：'))
for page in range(start_page,end_page+1):
    url='https://airport.supfree.net/index.asp?page='+str(page)
    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                                     " (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
    reques=requests.get(url,headers=headers).content.decode('gbk')
    html_concent=etree.HTML(reques)
    html_label=html_concent.xpath("//table[@class='ctable']/tr")[1:]
    s += 1
    for lobel in html_label:
        item={}
        item['城市名']=lobel.xpath('./td[1]//text()')[0] if (len(lobel.xpath('./td[1]//text()'))>0) else ''
        item['机场三字码']=lobel.xpath('./td[2]//text()')[0] if (len(lobel.xpath('./td[2]//text()'))>0) else ''
        item['机场四字码'] = lobel.xpath('./td[3]//text()')[0] if (len(lobel.xpath('./td[3]//text()')) > 0) else ''
        item['机场名称'] = lobel.xpath('./td[4]//text()')[0] if (len(lobel.xpath('./td[4]//text()')) > 0) else ''
        item['机场英文名称'] = lobel.xpath('./td[5]//text()')[0] if (len(lobel.xpath('./td[5]//text()')) > 0) else ''
        with open("D:\\机场三字码\\机场三字码.txt",'a+')as f:
            f.writelines(item['城市名']+'\t'+item['机场三字码']+'\t'+item['机场四字码']+'\t'+item['机场名称']+'\t'+item['机场英文名称']+'\n')
            f.close()
    print('正在爬第'+str(s)+'页')