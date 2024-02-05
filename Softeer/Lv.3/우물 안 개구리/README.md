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

<span>헬스장에서 N명의 회원이 운동을 하고 있다. 각 회원은 1에서 N사이의 번호가 부여되어 있고, i번 회원이 들 수 있는 역기의 무게는 W</span><sub><span class="EditorTheme__textSubscript">i</span></sub><span>이다. 회원들 사이에는 M개의 친분관계 (A</span><sub><span class="EditorTheme__textSubscript">j</span></sub><span>, B</span><sub><span class="EditorTheme__textSubscript">j</span></sub><span>)가 있다. (A</span><sub><span class="EditorTheme__textSubscript">j</span></sub><span>, B</span><sub><span class="EditorTheme__textSubscript">j</span></sub><span>)는 A</span><sub><span class="EditorTheme__textSubscript">j</span></sub><span>번 회원과 B</span><sub><span class="EditorTheme__textSubscript">j</span></sub><span>번 회원이 친분 관계가 있다는 것을 의미한다. i번 회원은 자신과 친분 관계가 있는 다른 회원보다 들 수 있는 역기의 무게가 무거우면 자신이 최고라고 생각한다. 단, 누구와도 친분이 없는 멤버는 본인이 최고라고 생각한다.</span>

<span>이 헬스장에서 자신이 최고라고 생각하는 회원은 몇 명인가?</span>  

</div>

</div>

</div>

<div class="detail-con-box">

##### 제약조건

# 

<span>2 ≤ N ≤ 10</span><sup><span class="EditorTheme__textSuperscript">5</span></sup>  
<span>1 ≤ M ≤ 10</span><sup><span class="EditorTheme__textSuperscript">5</span></sup>  
<span>1 ≤ W</span><sub><span class="EditorTheme__textSubscript">i</span></sub> <span>≤ 10</span><sup><span class="EditorTheme__textSuperscript">9</span></sup>  
<span>1 ≤ A</span><sub><span class="EditorTheme__textSubscript">j</span></sub><span>, B</span><sub><span class="EditorTheme__textSubscript">j</span></sub> <span>≤ N</span>  
<span>A</span><sub><span class="EditorTheme__textSubscript">j</span></sub> <span>≠ B</span><sub><span class="EditorTheme__textSubscript">j</span></sub>

</div>

<div class="detail-con-box">

##### 입력형식

# 

<span>첫 번째 줄에 두 정수 N, M이 주어진다.</span>  
<span>두 번째 줄에 N개의 정수 W</span><sub><span class="EditorTheme__textSubscript">1</span></sub><span>, W</span><sub><span class="EditorTheme__textSubscript">2</span></sub><span>, ... , W</span><sub><span class="EditorTheme__textSubscript">N</span> </sub><span>이 주어진다.</span>

<span>다음 M개의 줄의 j번째 줄에는 두 정수 A</span><sub><span class="EditorTheme__textSubscript">j</span></sub><span>, Bj 가 주어진다.</span>  

</div>

<div class="detail-con-box">

##### 출력형식

# 

<span>첫 번째 줄에 자신이 최고라고 생각하는 회원 수를 출력한다.</span>

</div>

<div>

<div class="detail-con-box">

##### 입력예제1

<pre>

#### 5 3
1 2 3 4 5
1 3
2 4
2 5

</pre>

</div>

<div class="detail-con-box">

##### 출력예제1

<pre>

#### 3

</pre>

</div>

</div>

<div>

<div class="detail-con-box">

##### 입력예제2

<pre>

#### 5 3
7 5 7 7 1
1 2
2 3
3 4

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