


Васильев Евгений

Домашнее задание к занятию "3.2. Работа в терминале, лекция 2"





1.) команда cd является коммандой для совершения переходов из директорий  и не относиться к stdin и stdout (как мне кажется).



2.) альтернативой команде grep <some_string> <some_file> | wc -l будет команда: grep -c "искомая строка" <имя файла>



3.) процесс systemd является родтителем для всех последующих процессов в системе, проверено pstree -p на виртуальной машине с Ubuntu 20.04



4.) данная команда ls > /dev/pts/1 обображает текущее содержимое каталога в соседнем терменеле, перенаправление, потока вывода, работает. 



5.)  echo $(<README.md) | tee -a text.out  - данная команда выводит файл README.md  в терминал (stdin)  и пишет в файл (stdout) в text.out файл  

    

6.) sudo echo Test from TTY pts0 > /dev/tty - ответ, это протестированно в эмуляторе терминала Tilix на виртуальной машине - vagrant, ubuntu 20.04 в режиме ssh
    


7.) команда bash 5>&1 ни к чему не привела визуально, кроме как создала дескриптор, а echo netology > /proc/$$/fd/5 вывела дескриптор (stdout) 5 в строке появилось  - netology, 
    в другом окне терминала повторный ввод команты приводит к ошибке "bash: /proc/4483/fd/5: Нет такого файла или каталога" так как перенаправление работает только с текущей сессией   



8.) ls -l my_folder 9>&2 2>&1 1>&9 |grep denied -c вот такая конструкция получилась учитывая предыдущий опыт 



9.) будут выведины переменные, а tail /proc/$$/environ  является альтернативой для отображения данной информации



10.) строка 231 в man proc - /proc/[pid]/cmdline путь до файла процесса и  /proc/[pid]/exe ссылка до файла процесса который запущен



11.) версию SSE 4.2



12.) у меня вывело /dev/pts/0 обращение команды ssh localhost 'tty'



13.) установил reptyr в Ubuntu 29.04, попытался следующей коммандой reptyr -T 31593 переместить процесс (vagrant) но он ругается -


     Unable to attach to pid 31593: Operation not permitted
The kernel denied permission while attaching. If your uid matches
the target's, check the value of /proc/sys/kernel/yama/ptrace_scope.
For more information, see /etc/sysctl.d/10-ptrace.conf


добавил sudo и все заработалор sudo reptyr -T 31593 в этом окне куда вводил открылось окно vagrant-а



14.) в 5. пункте этой домашки я уже использовал tee и sudo tee будет работать потому как команда tee читает из стандартного ввода и записывает как в стандартный вывод, так и в один или несколько
     файлов одновременно, а с sudo может конечно же писать и в root директорию.
