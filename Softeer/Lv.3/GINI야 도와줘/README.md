<div id="study_tab1" class="tab__pane tab-active" role="tabpanel" aria-labelledby="study_tab1" aria-hidden="false">

<div class="detail-con-box">

##### 언어별 시간/메모리

<div class="table-wrap">

<table class="table"><caption>언어별 시간/메모리 표</caption>

<thead>

<tr>

<th scope="col" id="t-lang">언어</th>

<th scope="col" id="t-time">시간</th>

<th scope="col" id="t-memory">메모리</th>

</tr>

</thead>

<tbody>

<tr>

<td headers="t-lang">JavaScript</td>

<td headers="t-time">1초</td>

<td headers="t-memory">256MB</td>

</tr>

<tr>

<td headers="t-lang">C</td>

<td headers="t-time">1초</td>

<td headers="t-memory">256MB</td>

</tr>

<tr>

<td headers="t-lang">C++</td>

<td headers="t-time">1초</td>

<td headers="t-memory">256MB</td>

</tr>

<tr>

<td headers="t-lang">Java</td>

<td headers="t-time">1초</td>

<td headers="t-memory">256MB</td>

</tr>

<tr>

<td headers="t-lang">Python</td>

<td headers="t-time">1초</td>

<td headers="t-memory">256MB</td>

</tr>

</tbody>

</table>

</div>

<div>

<div style="font-size: 1.6rem">

<span>GINI는 현대자동차그룹에서 개발한 네비게이션이다. GINI는 너무나도 뛰어나 목적지에 도착하는 시간을 예측할 수 있다. 어느 날 태범이는 세차장에서 세차를 하고 집에 돌아가려고 하는데 소나기가 몰려오고 있다는 뉴스를 전해 들었다. 태범은 방금 세차한 차를 지키기 위해 GINI를 사용하여 무사히 집에 귀환하고자 한다!</span>

<span>지도는 R행과 C열로 이루어져있다. 비어있는 칸은 ‘.’로 표시되고, 소나기는 ‘*’로, 강은 ‘X’로 표시되어있다. 태범이의 집은 ‘H’로 표현되고, 태범이가 처음있던 세차장의 위치는 ‘W’로 표시된다.</span>

<span>매 분마다 태범이는 인접한 네 개의 칸(상, 하, 좌, 우)으로 이동할 수 있다. 소나기는 매 분마다 인접한 네 개의 칸(상, 하, 좌, 우)으로 확산한다. 태범이는 소나기와 강을 지나지 못하며, 소나기는 강과 태범이의 집에 옮겨지지 않는다.(소나기는 강으로 가면 소멸) 태범이가 무사히 집에 도착할 수 있을 때 몇 분 만에 도착할 수 있는 예측하는 GINI 네비게이션 프로그램을 만들어보자.</span>

</div>

</div>

</div>

<div class="detail-con-box">

##### 제약조건

# 

<span>R, C ≤ 50</span>

<span>‘H’와,’W’는 하나씩만 주어진다.</span>

</div>

<div class="detail-con-box">

##### 입력형식

# 

<span>첫째 줄에 R과 C가 주어진다. 다음 N개 줄에는 지도가 주어지며, 문제에서 설명한 문자만 주어진다.</span>  

</div>

<div class="detail-con-box">

##### 출력형식

# 

<span>첫째 줄에 태범이가 집으로 갈 수있는 가장 빠른 시간을 출력한다. 만약 소나기를 피해 집에 도착할 수 없다면 “FAIL”을 출력한다.</span>  

</div>

<div>

<div class="detail-con-box">

##### 입력예제1

<pre>

#### 4 3
H.*
...
XXX
W..

</pre>

</div>

<div class="detail-con-box">

##### 출력예제1

<pre>

#### FAIL

</pre>

</div>

</div>

<div>

<div class="detail-con-box">

##### 입력예제2

<pre>

#### 3 3
H.*
...
W..

</pre>

</div>

<div class="detail-con-box">

##### 출력예제2

<pre>

#### 2

</pre>

</div>

</div>

</div>