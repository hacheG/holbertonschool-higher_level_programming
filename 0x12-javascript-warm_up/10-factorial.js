#!/usr/bin/node
function Factorial(a)
{
    let fac = 1;
    if (a == 1)
    {
        return 1;
    }
    else
    {
        for (let i=1; i<=a; i++)
        {
            fac = fac * i;
            
        }
        return fac;
    }
}
console.log(Factorial(parseInt(process.argv[2])));
