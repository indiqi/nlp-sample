# NLP sample

The purpose of the posted job is to create an AWS lambda function written in Python that encapsulates the functionality of the `humanise` function in main.py

You are to target Python versions >= 3.8.x

Note that I'm not locking any detail of the implementation - as long as it generates the same results, you are welcome to change the code in any way you see fit, while keeping to the instructions below.

Most specifically, vendorising the spaCy models is a bit of a hack - you are encouraged to use some other method of injecting the desired modules and models - lambda layers, for instance, are encouraged. Both English and Portuguese models are to be present.  

You are encouraged to use a framework such as Chalice, or Serverless, _with preference to Chalice_.

The code is **not** to download the models at runtime. It is, however, perfectly acceptable to do so at build time.

While spaCy is preferred, producing the same results with NLTK would also be acceptable.

