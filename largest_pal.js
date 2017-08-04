function findPal(arg,i,j)
{
    flag = 0;
    while (flag == 0)
    {
        if (arg[i] != "[a-z]" && arg[i] != undefined)
        {
            i -= 1;
        }
        else if (arg[j] != "[a-z]" && arg[j] != undefined)
        {
            j += 1;
        }
        else if (arg[i] == arg[j])
        {
            i-=1;
            j+=1;
        }
        else
        {
            i+=1;
            j-=1;
            flag = 1;
        }
    }
}
function longestPal(arg)
{
    max = arg[0];
    lower = arg.toLowerCase()
    for(var i =0; i < lower.length-3; i++){
        j = i;
        if(lower[i] == lower[i+1])
        {
            j += 1;
            findPal(lower,i,j);
        }
        else if(lower[i] == lower[i+2])
        {
            j += 2;
            findPal(lower,i,j);
        }
        if (max.length < (j-i+1))
        {
            max = lower.substring(i,j+1);
        }
    }
    return max;
}