# Toy Project_SHING

## 구현 준비

### 구현 1차 목표

지하철 출발역과 목표역을 받아서, 승차 시 이용할 수 있는 편의시설(엘리베이터, 에스컬레이터, 휠체어 리프트 등)을 알려주고 => 휠체어 전용공간이 있는 플랫폼으로 승차 위치를 안내한다.

출발역 - 경유역 - 목표역을 API를 통해 확인하고, 역 간 소요시간 및 경유 시의 편의 시설, 승하차 플랫폼 위치를 위와 같은 방법으로 안내한다.

목표역에서 하차 시, 사용하고자 하는 편의시설이 있는 위치를 알려주고, 점검, 보수 등으로 사용이 불가할 경우 검색 페이지에서 알려준다.



### 활용 API 및 정보 선정

1. 서울교통공사 편의시설 정보 - 휠체어리프트, 엘리베이터, 에스컬레이터 등 위치 정보
   - 서울교통공사 교통약자 승강기 가동 현황 : http://data.seoul.go.kr/dataList/OA-15994/A/1/datasetView.do;jsessionid=E1F13B183B3AC8DDBA5BEFA26BD3310C.new_portal-svr-11
   - 서울교통공사 휠체어경사로 설치 현황 : http://data.seoul.go.kr/dataList/OA-13116/S/1/datasetView.do
   - 서울교통공사 편의시설 현황 : http://data.seoul.go.kr/dataList/OA-13321/F/1/datasetView.do
   - 서울교통공사 휠체어 이용 승·하차 안내 : http://www.seoulmetro.co.kr/kr/page.do?menuIdx=769
   
2. 지하철 관련 정보
   - 대중교통 환승 경로 조회 - 지하철 : http://api.bus.go.kr/contents/sub02/getPathInfoBySubway.html
   
   - 서울특별시_대중교통환승경로 조회 서비스 : https://www.data.go.kr/data/15000414/openapi.do
   
   - 서울교통공사 환승역거리 및 소요 시간 정보 : http://data.seoul.go.kr/dataList/OA-13290/F/1/datasetView.do
   
   - 서울시 역코드로 지하철역별 열차 시간표 정보 검색 : https://data.seoul.go.kr/dataList/OA-101/A/1/datasetView.do => 추가 기능
   
   - 서울시 지하철 실시간 도착정보 : http://data.seoul.go.kr/dataList/OA-12764/F/1/datasetView.do (사용할지 안할지 모름) => 추가 기능
   
   - 역코드 및 좌표 정보 참조 :  https://observablehq.com/@taekie/seoul_subway_station_coordinate
   
   - 서울시 지하철역 정보 검색 (역명) : http://data.seoul.go.kr/dataList/OA-121/S/1/datasetView.do
   
     => 역명 및 코드 데이터 통일성을 위해 참조



### 발급 API 키 목록

1. 서울 열린데이터 광장
2. 공공데이터포털



=> 인증키 활용한 데이터 받기 성공. (5/15)

=> 모델 및 데이터 구조 설정 단계 필요.



### ERD 작성 및 모델, 자료 구조 파악 (5/16 ~ 5/17)

1. **서울특별시_대중교통환승경로 조회 서비스**(getLocationInfoList, getPathInfoBySubwayList) : OPEN API => json파일로 변환해야 하고, 환승경로 조회 및 총 소요시간 알 수 있다.

   ```python
   # 서울특별시 대중교통환승경로 조회 서비스 api 데이터 json으로 받아오기
   # 기능 : getLocationInfoList
   import requests
   import json
   from pprint import pprint
   
   url = 'http://ws.bus.go.kr/api/rest/pathinfo/getLocationInfo'
   params ={'serviceKey' : 'key', 'stSrch': '서울역','resultType' : 'json' }
   
   response = requests.get(url, params)
   res = response.content.decode('utf-8')
   pprint(res)
   # => 실제 주소지 좌표가 아니라 근처에 있는 버스정류장, 역을 검색해서 보여준다...
   
   # 기능 : getPathInfoBySubwayList
   import requests
   import json
   from pprint import pprint
   
   url = 'http://ws.bus.go.kr/api/rest/pathinfo/getPathInfoBySubway'
   params ={'serviceKey' : 'key', 'startX' :126.83948388112836, 'startY' : 37.558210971753226, 'endX' : 127.01460762172958, 'endY' : 37.57250, 'resultType' : 'json' }
   
   response = requests.get(url, params)
   res = response.json()
   pprint(res)
   ```

   - 인코딩 키와 디코딩 키 둘 중의 하나 구동되는 것을 적절히 사용하여야 함.
   - xml => json 파일 변환하기 고비 넘김. // 디코딩!!
   - gpsX, gpsY를 받아와야 할지 poiX, poiY를 받아와야 할지 고민하기.
   - 조회된 모든 환승 경로를 다 보여준다 => 그에 대한 선택이 가능하도록 옵션으로 표기!

2. **서울교통공사 환승역거리 및 소요시간 정보** : 파일

3. 서울교통공사 역간 거리 및 소요시간 정보 : OPEN API 

   => 직접 API 호출해보고 환승경로 여러번 호출이 나은지, 역간 거리 계산이 나은지 고려해보기

4. 서울시 역코드로 지하철역별 열차 시간표 정보 검색 :  open API 

   => 필터링으로 이 다음에 올 첫번째 열차 검색해서 보여줄 수 있음.

5. **모든 지하철역 X, Y 좌표 찾아서 데이터베이스 만들기** => 모델 : 데이터 넣어두기

   [역코드, 호선, 역이름, X좌표, Y좌표]

   --------------------------------------------------------------------------------지하철 최단 시간, 최소환승 경로 

5. **서울교통공사 교통약자 승강기 가동상황** : OPEN API => 10분마다 api 호출하여 데이터 업데이트

7. **서울시 편의시설 위치**(휠체어 경사로, 리프트, 엘리베이터, 에스컬레이터 각개) : json 파일

8. **휠체어 전용공간 및 안전발판** => 역 데이터 모델에 필드로 정보 삽입.

   ------------------------------------------------------------------------------------------------ 편의시설 관련



#### 사용자 선택사항 분류 

캐리어 => 1. 에스컬레이터 2. 엘리베이터 3. 빠른 환승 경로 4. 화장실(개찰구 안 지나고 갈 수 있는가)

유모차 => 1. 엘리베이터 2. 빠른 환승 경로 3. 수유실( + 기저귀 가는 곳)  (옵션으로 전동차 전용 공간 )

휠체어 및 전동차 => 1. 전동차 전용 공간(승하차 연단 간격 적은곳, 등등.. ) 2. 엘리베이터

( 경로 안내에 있어서는 엘리베이터 우선 고려, 승하차 위치 지정은 전동자 전용 공간 우선 고려)

--------------------------------------------------------------------------------------------------여기까지 필수!

자전거 => 1. 자전거 거치 가능한 차량칸 안내?? 2. 자전거 경사로 위치 3. 엘리베이터?





## 2차 구현 논의(5/17)

1. 경로안내
   - 경로 옵션으로 편의시설 상황에 따라 선택할 수 있도록 제공.
   - 환승역간 소요시간을 환승경로 API를 여러 번 호출해서 도출할 것인가, 역간소요시간 API를 사용해 도출할 것인가.
2. 편의시설 가동상황 정보 제공
   - 간단한 데이터 필터링으로 제공.



### 페이지 구성

1. HOME(INDEX)
2. 경로 안내
3. 경로 안내 상세 페이지
4. 편의시설 가동현황 확인 페이지
5. (추가사항) 게시판 기능 구현