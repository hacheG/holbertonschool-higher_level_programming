#!/usr/bin/node

if (isNaN(process.argv[2]))
{
    console.log('Missing number of occurrences');
}
else
{
    for (let i=0; i<parseInt(process.argv[2]); i++)
    {
        let ex = '';
        for (let j=0; j<parseInt(process.argv[2]); j++)
        {
            ex = ex + 'X';
        }
        console.log(ex);
    }
}