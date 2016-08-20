from distutils.core import setup

setup(
    name='ssjrecsys',
    version='1.0.0',
    #packages=[''],
    url='',
    license='suishou technology',
    author='aturbo',
    author_email='592559065@qq.com',
    description='this is a ',
    classifiers=[
         'Topic :: Recommendation System',
         'Topic :: Text Processing',
     ],
     keywords='recommender',
      packages=['ssjrecsys'],
      package_dir={'ssjrecsys':'ssjrecsys'},
      package_data={'ssjrecsys':['*.*','classifier/*','clustering/*','common/*','file/*','models/*','recommender/*','util/*']}
)