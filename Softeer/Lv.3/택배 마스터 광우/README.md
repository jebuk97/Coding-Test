<div class="tab__content">

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

<td headers="t-time">2초</td>

<td headers="t-memory">256MB</td>

</tr>

<tr>

<td headers="t-lang">C</td>

<td headers="t-time">2초</td>

<td headers="t-memory">256MB</td>

</tr>

<tr>

<td headers="t-lang">C++</td>

<td headers="t-time">2초</td>

<td headers="t-memory">256MB</td>

</tr>

<tr>

<td headers="t-lang">Java</td>

<td headers="t-time">2초</td>

<td headers="t-memory">256MB</td>

</tr>

<tr>

<td headers="t-lang">Python</td>

<td headers="t-time">2초</td>

<td headers="t-memory">256MB</td>

</tr>

</tbody>

</table>

</div>

<div>

<div style="font-size: 1.6rem">

<span>여름 휴가를 떠나기 위해 용돈이 필요했던 광우는 H택배 상하차 아르바이트를 지원 했다. 광우는 평소에 운동을 하지않아 힘쓰는 데에 자신이 없었지만, 머리 하나 만큼은 비상해 택배가 내려오는 레일의 순서를 조작해서 최소한의 무게만 들 수 있게 일을 하려고 한다.</span>  

<span>레일은 N개이며, 각각의 레일은 N</span><sub><span class="EditorTheme__textSubscript">i</span></sub> <span>무게 전용 레일로 주어진다. (같은 무게의 레일은 주어지지 않는다.) 레일의 순서가 정해지면 택배 바구니 무게(M)를 넘어가기 전까지 택배 바구니에 택배를 담아 들고 옮겨야 한다. 레일 순서대로 택배를 담되, 바구니 무게를 초과하지 않은 만큼 담아서 이동하게 되면 1번 일한 것으로 쳐준다. (단, 택배는 순서대로 담아야 하므로 레일의 순서를 건너 뛰어 담을 수는 없다)</span>  

<span>총 K번 일을 하는데 최소한의 무게로 일을 할 수 있게 광우를 도와주는 프로그램을 만들어 보자.</span>

</div>

</div>

</div>

<div class="detail-con-box">

##### 제약조건

# 

<span>3 ≤ N ≤ 10</span>

<span>max(N</span><sub><span class="EditorTheme__textSubscript">i</span></sub><span>) < M ≤ 50</span>

<span>1 ≤ K ≤ 50</span>

<span>1 ≤ N</span><sub><span class="EditorTheme__textSubscript">i</span></sub> <span>≤ 50</span>

</div>

<div class="detail-con-box">

##### 입력형식

# 

<span>첫째 줄에는 레일의 개수 N, 택배 바구니의 무게 M, 일의 시행 횟수 K가 주어진다. 그 다음 줄에는 N</span><sub><span class="EditorTheme__textSubscript">i</span></sub><span>개의 택배 레일의 전용 무게가 주어진다. (택배 바구니는 무조건 택배보다 작은 경우는 없다.)</span>  

</div>

<div class="detail-con-box">

##### 출력형식

# 

<span>출력으로는 광우가 일 해야하는 최소한의 택배 무게를 출력한다.</span>  

</div>

<div>

<div class="detail-con-box">

##### 입력예제1

<pre>

#### 5 20 4
5 8 10 19 7

</pre>

</div>

<div class="detail-con-box">

##### 출력예제1

<pre>

#### 54

</pre>

</div>

</div>

<div>

<div class="detail-con-box">

![](https://www.softeer.ai/upload/2021/06/20210630_131717865_44375.png)  

<span>레일의 개수가 5개이고 택배 바구니의 무게를 20, 일을 시행해야 하는 횟수를 4번 이라고 했을 때, 레일의 순서가 | 5 | 8 | 10 | 19 | 7 | 이 된다면 총 4번 수행 했을 때 답은 62가 된다.</span>

<span>1번 (5+8)</span>

<span>2번 (5+8) + (10)</span>

<span>3번 (5+8) + (10) + (19)</span>

<span>4번 (5+8) + (10) + (19) + (7+5+8) = 62</span>

<span>하지만 최적의 순서는 | 5 | 10 | 8 | 19 | 7 | 이 된다.</span>

<span>1번 (5+10)</span>

<span>2번 (5+10) + (8)</span>

<span>3번 (5+10) + (8) + (19)</span>

<span>4번 (5+10) + (8) + (19) + (7+5) = 54</span>


<hr/>

##### 입력예제2

<pre>

#### 9 25 50
1 21 2 22 3 23 4 24 10

</pre>

</div>

<div class="detail-con-box">

##### 출력예제2

<pre>

#### 772

</pre>

</div>

</div>

</div>

</div>