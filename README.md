####################################
### Васильев Евгений,  devops-26
####################################


# Домашнее задание к занятию "3.3. Операционные системы. Лекция 1"

------

## Ответы на задания:

1. chdir("/tmp") = 0


2. openat(AT_FDCWD, "/usr/share/misc/magic.mgc", O_RDONLY) = 3
   

3. мы находим процесс удаленного файла, 
   выявляем его дискриптор ( пример /proc/$$/fd/5 (stdout) дескриптор 5)
   далее отправляем пустую строку в дескриптор echo ' ' > /proc/$$/fd/5

4. Нет, зомби процессы не потребляют ресурсы, когда процесс завершается через exit, вся память и связанные с ним ресурсы освобождаются, чтобы их могли использовать другие процессы.


5. ```bash 
   vagrant@ubuntu2204:~$ dpkg -L bpfcc-tools | grep sbin/opensnoop
   /usr/sbin/opensnoop-bpfcc
   vagrant@ubuntu2204:~$ sudo /usr/sbin/opensnoop-bpfcc
   
   PID    COMM               FD ERR PATH
   728    vminfo              4   0 /var/run/utmp
   613    dbus-daemon        -1   2 /usr/local/share/dbus-1/system-services
   613    dbus-daemon        20   0 /usr/share/dbus-1/system-services
   613    dbus-daemon        -1   2 /lib/dbus-1/system-services
   613    dbus-daemon        20   0 /var/lib/snapd/dbus-1/system-services/
   728    vminfo              4   0 /var/run/utmp
   613    dbus-daemon        -1   2 /usr/local/share/dbus-1/system-services
   613    dbus-daemon        20   0 /usr/share/dbus-1/system-services
   613    dbus-daemon        -1   2 /lib/dbus-1/system-services
   613    dbus-daemon        20   0 /var/lib/snapd/dbus-1/system-services/
   620    irqbalance          6   0 /proc/interrupts
   620    irqbalance          6   0 /proc/stat
   620    irqbalance          6   0 /proc/irq/20/smp_affinity
   620    irqbalance          6   0 /proc/irq/0/smp_affinity

6.  a.) strace uname -a

```bash
 uname({sysname="Linux", nodename="ubuntu2204.localdomain", ...}) = 0
 write(1, "Linux ubuntu2204.localdomain 5.1"..., 122Linux ubuntu2204.localdomain 5.15.0-41-generic #44-Ubuntu SMP Wed Jun 22 14:20:53 UTC 2022 x86_64 x86_64 x86_64 GNU/Linux 
```
b.) man uname(2) line 65:

Part of the utsname information is also accessible via /proc/sys/kernel/{ostype, hostname, osrelease, version, domainname}.

7. оператор ";" - используется для последовательного выполнения команд типа ls /dir/; cd /dir/ 

"&&" - оператор может быть выполнена таким образом: echo hi && echo hello выполнется даже если завершится ошибкой
сначала выполняется первая команда "echo hi", если оно завершено без ошибки то выполняется следующая команда после оператора "&&" - "echo hello" 

"set -e" - смысл есть, выход если команда выполнена со статусом "0" т.е. без ошибок, если Если ошибочно завершится одна из команд, разделённых &&, то выхода из оболочки не будет.


8. -e прерывает выполнение исполнения при ошибке любой команды кроме последней в последовательности;
-x вывод трейса простых команд;
-u неустановленные/не заданные параметры и переменные считаются как ошибки, с выводом в stderr текста ошибки и выполнит завершение не интерактивного вызова;
-o pipefail возвращает код возврата набора/последовательности команд, ненулевой при последней команды или 0 для успешного выполнения команд.

Повышает детализацию вывода ошибок и завершит сценарий при наличии ошибок, на любом этапе выполнения сценария, кроме последней завершающей команды.


9. ps -Ao stat  | sort | uniq -c | sort -h
```bash
   1 Sl
   1 SLsl
   1 S<s
   1 Ss+
   1 STAT
   2 R+
   2 S+
   2 SN
   6 Ssl
   11 I
   13 Ss
   27 S
   40 I<

I - фоновые процессы ядра
S - спящие процессы, находятся в режиме ожидания

----

