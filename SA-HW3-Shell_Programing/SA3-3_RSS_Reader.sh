#! /bin/sh
itemlist=''
itemflag=''
Read2(){
    count=0
    h=$(eval echo ~$user)
    d='/.feed/content/*'
    mypath=$h$d
    for i in $mypath;do
        count=$((count+1))
        if [ $count == $1 ];then
            i=$(echo $i | rev | cut -d \/ -f1 | rev)
            file=$i
        fi
    done
while [ true ]
do
if [ -z $itemflag ]
then
    itemflag='ok'
    itemlist=''
    #Read Rss Titles From File
    d='/.feed/content/'
    file=$h$d$file
    count=0
    IFS=\*
    while read line;do
        tmp=$(echo $line | awk '{ print $0}' | grep item_ | cut -d \_ -f2 | cut -c1-50)
        [ -z $tmp ] && continue
        count=$((count+1))
        itemlist="$itemlist $count*$tmp*"
    done < "$file"
fi
    IFS=\*
    dialog --title "Read" --menu "Choose article" 24 100 20 $itemlist 2>"${opt}"
    IFS=\
    read ch<$opt
    [ -z $ch ] && break

    #Ready to show message
    count=0
    c2=0
    content=''
    while read line;do
        IFS=\*
        tmp=$(echo $line | awk '{ print $0}' | grep item_ )
        [ $tmp ] && count=$((count+1))
        if [ $count ==  $ch ]
        then
            if [ $c2 == 0 ];then
                text=$(echo $line | awk '{ print $0}' | grep item_ | cut -d \_ -f2 )
                content="$content $text\n=========================================================================\n"
            elif [ $c2 == 1 ];then
                text=$(echo $line)
                content="$content Feed URL: $text\n=========================================================================\n"
            else
                text=$(echo $line)
                content="$content $text\n"
            fi
            c2=$((c2+1))
        fi
    done < "$file"
    content="$content \n=========================================================================\n"

    dialog --msgbox "$content" 48 120

    IFS=\
done
}

Read(){
while [ true ]
do
        count=0
        mylist=''
        itemflag=''
        h=$(eval echo ~$user)
        d='/.feed/content/*'
        mypath=$h$d
        for i in $mypath; do
            count=$((count+1))
            i=$(echo $i | rev | cut -d \/ -f1 | rev)
            mylist="$mylist $count*$i*"
        done
        #echo $mylist
        IFS=\*
        dialog --title "Read" --menu "Choose Subscrition" 20 80 $count $mylist 2>"${opt}"
        IFS=\
        read tmp<$opt
        [ -z $tmp ] && break
        Read2 $tmp
done
    Main
}

Subscribe(){
    dialog --title "Subscribe" --inputbox "Enter feed url" 8 60 2>"${opt}"
    read tmp<$opt
    if [ -z $tmp ]
    then
        dialog --msgbox "NO Input Url! " 8 60
    else
        env python craw.py $tmp
    fi
    Main
}

Delete(){
    count=0
    mylist=''
    h=$(eval echo ~$user)
    d='/.feed/content/*'
    mypath=$h$d
    for i in $mypath; do
        count=$((count+1))
        i=$(echo $i | rev | cut -d \/ -f1 | rev)
        mylist="$mylist $count*$i*"
    done
    IFS=\*
    dialog --title "Delete" --menu "Choose one to Delete" 20 80 $count $mylist 2>"${opt}"
    IFS=\

    h=$(eval echo ~$user)
    d='/.feed/content/*'
    mypath=$h$d
    read tmp<$opt
    count=0
    for i in $mypath; do
        count=$((count+1))
        IFS=\:
        [ $count == $tmp ] && rm $i && dialog --msgbox "OK!" 8 60
        IFS=\
    done
    Main
}

Update(){
    count=0
    mylist=''
    h=$(eval echo ~$user)
    d='/.feed/content/*'
    mypath=$h$d
    okpath=$mypath
    state="off"
    for i in $mypath; do
        count=$((count+1))
        i=$(echo $i | rev | cut -d \/ -f1 | rev)
        mylist="$mylist$count*$i*$state*"
    done
    IFS=\*
    dialog --title "Update" --checklist "Choose one to Update" 20 80 $count $mylist 2>"${opt}"
    IFS=\

    mypath=$okpath
    read t<$opt
for tmp in $t;
do
    tmp=$(echo $tmp | cut -d \" -f2)
    count=0
    for i in $mypath; do
        count=$((count+1))
        if [ $count == $tmp ];then
            i=$(echo $i | rev | cut -d \/ -f1 | rev)
            h2=$(eval echo ~$user)
            d2='/.feed/content/.'
            url=$h2$d2$i
            IFS=\*
            url=$(cat $url)
            env python craw.py $url
            IFS=\
        fi
    done
done
    Main
}

Main(){
    dialog --title "Main Menu" --menu "Choose Action" 15 55 5 \
    R "Read - read subscribed feeds" S "Subscribe - new subscription" D "Delete - delete subscription" U "Update - update subscription" Q "Bye Bye" 2>"${opt}"
    read tmp<$opt
    case $tmp in
        R) Read;;
        S) Subscribe;;
        D) Delete;;
        U) Update;;
        Q) exit 1;;
    esac
}
p1=$(eval echo ~$user)
p2='/.feed/welcome.txt'
p3=$p1$p2
opt=opt.sh
dialog --textbox $p3 30 70
Main

rm -f $opt
