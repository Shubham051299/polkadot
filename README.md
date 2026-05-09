Write a `computePolkadotScore` function that counts the number of polkadots on the dress within the following ascii art of Angelica. 

Polkadots whose x coordinate is >= the x coordinate of the character that starts Angelica's lips and <= the x coordinate of the character that ends her lips are counted in a special way: multiply the sum of the polkadots in that range by the number of characters used to represent both of her pupils.

The final score could be computed with this formula:

```
Num Polkadots Outside the Lips Range + (Num Polkadots Inside the Lips Range) * (Num Chars Used to Represent Angelica's Pupils)
```

