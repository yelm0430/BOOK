# Project Plan
|날짜|해야할것|달성률|아쉬운 점|
|---|---|---|---|
|04/11|1. progect 생성|O|
||2. README 구성(컨셉,모델링,기능,개발)|▵|
||3. blog / urls.py 구현|▵|
|04/12| 1. 프로젝트 구상|O||
||2. README 구성(컨셉,모델링,기능,개발)|▵| 아직 모델링이 완벽하지 않음, 더 세부적인 모델링 필요
|04/13|1. 이전것 갈아엎음|
||2. 새로운 프로젝트 구상 -> 중고 전공 책 판매|O|
||3. README 구성(컨셉,모델링,기능,개발)|O|아직 M:N 관계가 헷갈림, 코드 작성하며 좀더 세부적인 관계 작성 필요 
||4. settings.py 설정(blog,user)|O|
||5. blog / urls.py 작성|~||
||5. blog / views.py 작성|~||



## Project : `중고 책 판매 사이트`
### - app name : `book`
#### - 설명 : 필요없는 전공 책을 판매 및 구매 가능한 사이트 
#### - 핵심 기능 : 타 사용자들의 관심 수 확인(나중에는 인기있는 전공책까기 확인 가능할 듯)
#### - `구현기능`
---
|로그아웃|기능|
|---|---|
|로그아웃 O|홈으로 redirect|
----
|로그인|기능|세부사항||
|---|---|---|---|
|로그인 O | 사이트 사용 가능
||조회수 확인
||관심수 확인
||댓글 작성|1.POST로 작성
|||2. form 유효|게시글 저장
||||detail_reply으로 redirect
||댓글 삭제|작성자 = 로그인한 사람이라면|detail_reply으로 redirect|
|로그인 x | 1. 로그인으로 redirect
||2. 아이디도 없다면 -> 회원가입으로 redirect
----

|구현기능|작성자 = 로그인한 사람 여부|기능|세부 사항|어디로 보낼지|
|---|---|---|---|---|
|게시글|O|작성(create)|1. POST로 작성
||||2. form 유효 |게시글 저장
|||||detail_posting으로 redirect
||X||| home으로 render
||O|수정(update)|1. POST로 작성
||||2. form 유효 |게시글 저장
|||||detail_posting으로 redirect
||X||| index_posting 으로 redirect
||O|삭제(delete)||index_posting으로 redirect
||X||| index_posting으로 redirect
---
#### MODEL
- blog
    - Article
        - title = char()
        - content = char()
        - created_at = datetime()
        - updated_at = datetime()

    - Reply
        - content = char()
        - posting = char()
        - created_at =datetime()


- accounts
    - id = char()
    - user_password =char()
    - user_email = char()


  
