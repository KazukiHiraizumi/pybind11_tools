# Pybind11+Open3D

## Pybindのインストール  
サブディレクトリにてpybind11を展開する
~~~ 
git clone https://github.com/pybind/pybind11.git
~~~
Pybind11のインスト
~~~
pip3 install pybind11
~~~
pybindというパッケージもあるので注意。必ず*11*を付けること。

## Open3D(C++)のインストール(Build from source)  
ソースコードをClone
~~~
git clone https://github.com/isl-org/Open3D
~~~
CMakeは19以上が要ります。必要なら以下にて最新へアップグレード
~~~
pip3 install cmake --upgrade
~~~
CloneしたOpen3DをCMakeする。
~~~
cd Open3D
mkdir build
cd build
cmake ..
~~~
Makeする
~~~
make -j$(nproc)
~~~
Installする
~~~
sudo make install
~~~

## ExampleのBuild  
サブディレクトリで個々にビルドする。例えば"ndarray2D"だと以下のとおり
~~~
cd ndarray2D
cmake .
make
~~~

## Exampleのテスト  
~~~
./test.py
~~~
または
~~~
python test.py
~~~

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


