# Linux Operation and Management - 1. Filesystem
리눅스 운영과 관리 첫 번째 시간~~??강의도 아니고~~에는 파일시스템에 대해서 알아볼 것이다.

## 파일시스템이란?
파일시스템(Filesystem)은 컴퓨터의 운영체제에서 하드디스크를 효과적으로 관리하고 파일이나 자료를 쉽게 발견 및 접근할 수 있도록 보관 또는 조직하는 구조를 가리키는 말이다.</br>

## 파일시스템의 종류
운영체제마다 지원하는 파일시스템이 상이하므로 다양한 종류가 있다. 대부분의 운영체제에서는 다양한 파일시스템을 지원한다.</br>
셤에는 안나오지만 NTFS, EXT, NFS, HFS, HFS+ Reiserfs, JFS, XFS 등등이 있다.

## 파일시스템 관련 명령어

# chmod
chmod (change mode)
```bash
 $ chmod [option] [mode] [filename]
```
<strong>chmod</strong> 명령어는 <strong>파일이나 디렉토리의 파일 허가권을 변경</strong>하는 데 사용된다.</br>
<strong>파일 허가권</strong>(Permission)은 파일이나 디렉토리에 대한 각 사용자의 허가와 권한을 나타낸다.</br>

#### option

- <strong>-R</strong> : 하위 디렉토리를 포함하여 디렉토리 내부의 모든 파일의 접근 권한을 변경(재귀적으로)
- <strong>-c</strong> : 권한이 바뀐 파일만 자세히 기술
- <strong>-f</strong> : 파일의 권한이 바뀔 수 없어도 에러 메세지를 출력하지 않음

#### mode
파일 시스템에는 3자리로 이루어진 권한 설정이 사용된다.

- 첫번째 자리 : <strong>파일 소유자(user)</strong>의 파일 허가권
- 두번째 자리 : <strong>그룹(group)</strong>의 파일 허가권
- 세번째 자리 : <strong>그 외 사용자(other users)</strong>의 파일 허가권

각 사용자의 권한은 4, 2, 1의 숫자 조합 또는 알파벳을 통해 나타낸다.

- <strong>r</strong> (read, 읽기) : 4
- <strong>w</strong> (write, 쓰기) : 2
- <strong>x</strong> (execute, 실행) : 1
- <strong>1000</strong> : 파일에 Sticky Bit를 적용
- <strong>2000</strong> : 파일에 SetGID를 적용
- <strong>4000</strong> : 파일에 SetUID를 적용

# umask
```bash
 $ umask [option] [value]
```
<strong>umask</strong>는 새로 만들어진 파일의 파일 권한을 어떻게 설정할지를 제어하는 데 사용하는 명령어이다.</br>
일반 파일이 가질 수 있는 최대 접근 권한은 666, 디렉토리는 777이다. </br>
umask 에 의해 각 기본권한에서 umask 값만큼 권한이 제한되므로 아래 같은 계산이 가능하다.</br>

- (해당 파일의 허가권) = 666 - (umask값)
- (해당 디렉토리의 허가권) = 777 - (umask값)

리눅스의 기본 umask 값은 022 또는 002이다.

#### option

- <strong>-S</strong> : 값을 문자로 표기

```bash
C:\Users\JunhoYeo>bash
JunhoYeo@DESKTOP-VKETEKB:/mnt/c/Users/JunhoYeo$ umask -S
u=rwx,g=rwx,o=rwx
```
직접 실행해 보아따.

# 특수 접근 권한
### SetUID
파일이 실행되는 동안 소유자의 권한으로 실행되게 한다.</br>
설정하는 퍼미션의 제일 앞에 4를 붙이면 된다. </br>
user권한에 s가 추가된다.

### SetGID
파일이 실행되는 동안 그룹의 권한으로 실행하게 한다.</br>
설정하는 퍼미션의 제일 앞에 2를 붙이면 된다. </br>
user권한에 s가 추가된다.

### Sticky Bit
모든 사용자가 삭제를 제외한 모든 권한을 가지게 한다.</br>
즉 디렉토리에 적용될 경우 누구나 해당 디렉토리에 파일을 생성할 수 있게 되는 것이다.</br>
설정하는 퍼미션의 제일 앞에 1를 붙이면 된다. </br>
user권한에 t가 추가된다.

# chown
chown (change owner)
```bash
 $ chown [option] [username] [filename]
```
또는
```bash
 $ chown [option] [username].[groupname] [filename]
```
chown 명령어는 파일의 소유자나 소유 그룹을 변경하기 위해서 사용된다.

#### option
- -R : 하위 디렉토리를 포함하여 디렉토리 내부의 모든 파일의 소유주와 소유 그룹을 변경(재귀적으로)
- -c : 변경된 정보를 출력

# chgrp
chgrp (change group)
```bash
 $ chgrp [option] [groupname] [filename]
```
chgrp 명령어는 파일 또는 디렉토리의 소유 그룹을 변경하기 위해서 사용된다.

#### option
- -R : 하위 디렉토리를 포함하여 디렉토리 내부의 모든 파일의 그룹 소유권을 변경(재귀적으로)
- -c : 변경된 정보를 출력

## 파일시스템 관련
#
