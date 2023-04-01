## Sigmaplot.py

## 소개
sigmaplot.py는 시그마 플롯의 rectangular hyperbola를 파이썬으로 그릴 수 있는 프로그램입니다. 이 프로그램은 pandas, scipy, matplotlib, seaborn 라이브러리를 사용하여 데이터를 처리하고 그래프를 그립니다.

<br>

## 설치
sigmaplot.py를 사용하기 위해서는, pandas, scipy, matplotlib, seaborn 라이브러리가 설치되어 있어야 합니다. 이 라이브러리들은 일반적으로 pip 명령어를 통해 설치할 수 있습니다.

```python
pip install pandas
pip install scipy
pip install matplotlib
pip install seaborn
```

<br>

## 사용법
sigmaplot.py는 input 폴더에 있는 xlsx 또는 csv 파일을 읽어와 그래프를 그립니다. 개별 파일을 입력하거나, input 폴더에 있는 모든 파일을 처리할 수 있습니다.

### 개별 파일 입력
개별 파일 입력(yes)을 선택하면, 파일 이름을 입력하라는 메시지가 출력됩니다. 이때, 파일 이름은 input 폴더에 있는 파일 이름과 동일해야 합니다.


### 모든 파일 입력
모든 파일 입력(no)을 선택하면, input 폴더에 있는 모든 xlsx 또는 csv 파일을 자동으로 처리합니다.


### 코드 실행
sigmaplot.py를 실행하면, 파일 입력 방식을 선택하는 메시지가 출력됩니다. 파일 입력 방식을 선택하면, 처리 중인 파일 이름과 결과가 출력됩니다. 결과 그래프는 output 폴더에 파일 이름.png 형식으로 저장됩니다.

<br>

## 함수 설명

### func
func 함수는 데이터를 입력받아 y0, a, b 값을 최적화합니다. 최적화는 scipy.optimize.differential_evolution 함수를 사용합니다.


### cal
cal 함수는 입력 파일과 S 값(Ca-S 데이터)을 입력 받습니다. 이 함수는 func 함수를 호출하여 최적화된 y0, a, b 값을 반환합니다.


### plot
plot 함수는 입력 파일, 결과를 저장할 폴더 이름, 파일 이름을 입력 받습니다. 이 함수는 cal 함수를 호출하여 최적화된 y0, a, b 값을 사용하여 그래프를 그립니다.


### main
main 함수는 프로그램의 메인 함수입니다. 파일 입력 방식을 선택하는 메시지를 출력하고, 선택한 방식에 따라 input 폴더의 파일들을 처리합니다.

<br>

## 결과

### SigmaPlot
![image](https://user-images.githubusercontent.com/93086581/229191234-1ef96e2e-7e1f-470d-821c-4c89894f94d2.png)

<br>

### SigmaPlot-Python
![9월100동](https://user-images.githubusercontent.com/93086581/229272576-9a76ddd7-d3b2-4357-bf30-8985dd7e9c67.png)