Васильев Евгений

Домашнее задание к занятию "3.2. Работа в терминале, лекция 2"





1.) установил VirtualBox (Oracle)


2.) установил Vagrant


3.) пользуюсь многооконным терминалом Tilix (https://gnunn1.github.io/tilix-web/)


4.) создал внутри каталога devops-netology каталог vagrant, отредактировал файл Vagrantfile, далее запустил vagrant init затем vagrant up и vagrant shh - попал в свою виртуалку


5.) по умолчанию выделенны следующие ресурсы:

    
    оперативная память 1024 Мб

    процессор  2

    жесткий диск 62.55 GiB


6.) добавить оперативку можно так в Vagrantfile

     config.vm.customize [
                        "modifyvm", :id,
                        "--name", "Test_Environment",
                        "--memory", "1024"
                      ]

7.) Выполнил vagrant ssh, внутри в командной строке в своем терминале проделал выполнение некоторых команд типа ls, ls -a, cd, fdisk -l и прочие ...


8.) Ознакомился с man bash

   a) Переменной HISTSIZE  можно задать длинну журнала history, описывается это на 936 строке мануала man bash
   
   b) значение ignoreboth - это сокращение от «ignorespace» и «ignoredups», например если установить в переменную это значение,  то строки, начинающиеся с пробела и   дубликаты, не будут сохранены


9.) {} позволяют объединить несколько операторов в один составной, это один из условных знаков, помогающих сократить количество писанины в командной строке в man bash информация находится на 442 строке в разделе Function name, искал в man bash вот так (man bash и далее /braces)


10.) touch a{1..100000} 100000 файлов создает спонойно, но 300000 не может создать, выдает ошибку - touch a{1..300000} Слишком длинный список аргументов, это происходит по причине, что файлов больше чем допустимый лимит, допустимый лимит можно проверить командой getconf ARG_MAX


11.) [[ -это улучшение bash по сравнению с командой [,  больше не нужно цитировать переменные, потому что [[ обрабатывает пустые строки и строки с whitespace более интуитивно
     [[ -d /tmp ]] проверяет условие в данном случае наличие каталога, сделал небольшой скрипт на этот случай

     #!/bin/bash

if [[ -d /tmp ]]; then 
echo "Каталог существует!"
else
echo "Каталог не существует!"
fi

12.) 
   a) создал каталоги $HOME:tmp/netology

   б) скопировал bash cp /bin/bash home/vagrant/tmp/netology

   в) добавил переменную PATH=$PATH:home/vagrant/tmp/netology
   получил вывод: type -a bash 

   bash is /usr/bin/bash

   bash is /bin/bash

   bash is /home/vagrant/tmp/netology/bash 
   
   (не разобрался только как первой строкой поставить)



13.) Команда at используется для назначения одноразового задания на заданное время, а команда batch — для назначения одноразовых задач, которые должны выполняться, когда загрузка системы становится меньше 1,5


14.) выключить виртуалку можно коммандой init 0 (обычно так и выключаю)