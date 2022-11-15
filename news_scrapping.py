# pip install newspaper3k
from newspaper import Article
import nltk
import url_collector

nltk.download('punkt')

# 파싱할 뉴스 기사 주소
news_lists = url_collector.update_news()
exist_url =[] # 기존에 존재하는 URL을 모아둠 (중복 조회시 패스하려고)

for title, url in news_lists:
    if url in exist_url:
        print("Exist Article")
    else:
        exist_url.append(url)

        # 언어가 한국어이므로 language='ko'로 설정
        article = Article(url, language='ko')
        article.download()
        article.parse()
        article.nlp()

        # 기사 정보
        author = article.authors # 글쓴이
        publish_date = article.publish_date # 발행 일자
        keywords = article.keywords # 키워드
        summary = article.summary # 요약
        text = article.text # 내용

        print()
        print(title)
        print(url)
        print(publish_date)
        print(summary)