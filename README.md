###########################
### Васильев Евгений    ###
###########################
###  devops-netology    ###
###########################
###########################
###########################

# TEST

---------------------------------


Домашнее задание к занятию "3.2. Работа в терминале, лекция 2"





1.) команда cd - это встроенная команда bash и относиться к типу stdin, команда запрашивает ввод от пользователя, поэтому я считаю ее преглашением к вводу от пользователя - stdin и нужна эта    команда для внутреннего перехода по каталогам и команде для этого нужны аргументы.



2.) альтернативой команде grep <some_string> <some_file> | wc -l будет команда: grep -c "искомая строка" <имя файла>



3.) процесс systemd является родтителем для всех последующих процессов в системе, проверено pstree -p на виртуальной машине с Ubuntu 20.04



4.) данная команда ls > /dev/pts/1 обображает текущее содержимое каталога в соседнем терменеле, перенаправление, потока вывода, работает. 



5.)    cat < hello > hello.out

    

6.) sudo echo Test from TTY pts0 > /dev/tty - ответ, это протестированно в эмуляторе терминала Tilix на виртуальной машине - vagrant, ubuntu 20.04 в режиме ssh
    


7.) команда bash 5>&1 ни к чему не привела визуально, кроме как создала дескриптор, а echo netology > /proc/$$/fd/5 вывела дескриптор (stdout) 5 в строке появилось  - netology, 
    в другом окне терминала повторный ввод команты приводит к ошибке "bash: /proc/4483/fd/5: Нет такого файла или каталога" так как перенаправление работает только с текущей сессией   



8.) ls -l my_folder 9>&2 2>&1 1>&9 |grep denied -c вот такая конструкция получилась учитывая предыдущий опыт 



9.) будут выведины переменные, а printenv, env  является альтернативой для отображения данной информации



10.) строка 231 в man proc - /proc/[pid]/cmdline Этот файл только для чтения содержит полную командную строку для процесса и строка 285 /proc/[pid]/exe этот файл представляет собой символическую   ссылку, содержащую фактический путь к выполняемой команде.



11.) версию SSE 4.2



12.) Чтобы успешно подключаться по ssh к себе же ( на локалхост) нужно добавить публичный ключ (~/.ssh/id_rsa.pub) в конец файла ~/.ssh/authorized_keys



13.) sudo reptyr -T (ввел PID vagrant) в окне в котором ввел команду отобразился процесс -vagrant



14.)  tee и sudo tee будет работать потому как команда tee читает из стандартного ввода и записывает как в стандартный вывод, так и в один или несколько
     файлов одновременно, а с sudo может конечно же писать и в root директорию.
