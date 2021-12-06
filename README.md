# Pybind11やってみよう

## パッケージのインストール
~~~
pip3 install pybind11
~~~
pybindというパッケージもあるので注意。必ず*11*を付けること。
## Exampleのインスト
~~~
git clone https://github.com/tdegeus/pybind11_examples.git
~~~
pybind11_examplesディレクトリの中の、pybind11ディレクトリにヘッダとかがインストされれはずだが、うまく行かないことがある。  
そういうときはpybind11_examples/にてpybind11をcloneする。
~~~
git clone https://github.com/pybind/pybind11.git
~~~
## ExampleのBuild  
Exampleディレクトリで個々にビルドする。例えば"01_py-list_cpp-vector"だと以下のとおり
~~~
cd 01_py-list_cpp-vector
cmake .
make
~~~

## Exampleのテスト  



## やっぱだめというときは

ソースビルドとか
~~~
sudo apt install pybind11-dev
~~~

~~~
git clone https://github.com/pybind/pybind11.git
cd pybind11
mkdir build &amp;&amp; cd build
cmake .. -DCMAKE_INSTALL_PREFIX=../install/ -DPYBIND11_TEST=Off
make install
~~~


