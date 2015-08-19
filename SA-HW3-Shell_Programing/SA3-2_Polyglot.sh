#!/bin/sh
usage(){
    echo "polyglot.sh [-h] [-s src] [-o output_name] [-l lang] [-c compiler]"
}

# Parse the arguments
while getopts ":hs:o:l:c:" opt;
do
    case "$opt" in
        h)  usage
            exit 1 ;;
        s)  iFile=$OPTARG ;;
        o)  oFile=$OPTARG ;;
        l)  lang=$OPTARG ;;
        c)  comp=$OPTARG ;;
        :)  echo "Error :-$OPTARG requires an argument"
            usage
            exit 1 ;;
        ?)  echo "Error : unknow option -$OPTARG"
            usage
            exit 1;;
        *)  exit 1 ;;
    esac
done
if [ ! -f "$iFile" ];then
    echo "Error: Source File not found!"
    usage
    exit 1
fi
#Replace "," with space(Reltive for loop)
list=$(echo "$lang"  | sed 's/,/\ /g')

#User Have Selected Language?
if [ -z $lang ]
then echo "Please select a language!"
    usage
    exit 1
fi

check=0
for j in $list
do
    if [ $j == c ] || [ $j == C ]
        then check=1
    elif [ $j == cc ] || [ $j == cpp ] || [ "$j" == "c++" ] || [ "$j" == "C++" ]
        then check=1
    fi
done

#echo "Language List:$list"
#echo "List have C? :$check"

#Only C & C++ have -c option
if [ $check == 0 ] && [ $comp ]
    then echo "Error: -c is for C/C++'s Compiler "
    exit 1
    usage
fi

#Check language list
for i in $list
do
    if [ $i == c ] || [ $i == C ]
    then
        #Set Default outFile
        if [ -z $oFile ]
        then oFile=sa.out
        fi
        #If compiler selected
        if [ $comp ]
        then
            #echo "MY Compiler:$comp"
            if [ $comp == gcc ] || [ $comp == clang ]
            then
                echo "HI~C ok"
                env $comp -o $oFile $iFile && ./$oFile
            #Wrong compiler call
            else
                    echo "Unknow Compiler:$comp for C"
            fi
        #Use Default compiler
        else
            env clang -o $oFile $iFile && ./$oFile
        fi
    #C++
    elif [ $i == "C++" ] || [ $i == cpp ] || [ $i == "c++" ] || [ $i == cc ]
    then
        if [ -z $oFile ]
        then oFile=sa.out
        fi

        if [ $comp ]
        then
            #echo "MY Compiler:$comp"
            if [ $comp == "g++" ] || [ $comp == "clang++" ]
            then
                env $comp -o $oFile $iFile && ./$oFile
            else
                    echo "Unknow Compiler:$comp for C++"
            fi
        else
            env g++ -o $oFile $iFile && ./$oFile


        fi
    elif [ $i == awk ] || [ $i == AWK ]
        then env awk -f $iFile
    elif [ $i == perl ] || [ $i == Perl ]
        then env perl $iFile
    elif [ $i == python ] || [ $i == Python ] || [ $i == py ] || [ $i == python2 ] || [ $i == Python2 ] || [ $i == py2 ]
        then env python2 $iFile
    elif [ $i == python3 ] || [ $i == Python3 ] || [ $i == py3 ]
        then env python3 $iFile
    elif [ $i == ruby ] || [ $i == Ruby ] || [ $i == rb ]
        then env ruby $iFile
    elif [ $i == Haskell ] || [ $i == haskell ] || [ $i == hs ]
        then env runhaskell $iFile
    elif [ $i == lua ] || [ $i == Lua ]
        then env lua52 $iFile
    elif [ $i == bash ] || [ $i == Bash ]
        then env bash $iFile
    else
        echo "Error:Unknow language: $i"
    fi
done
