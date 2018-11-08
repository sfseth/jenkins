node {
   stage('Prepare'){
   echo 'Preparation stage' 
   //sh 'sudo yum install -y python-pip && sudo yum install -y pytest'
   sh 'curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python get-pip.py'
   sh 'pip install pytest'
   }
   stage('Test'){
   echo 'Test stage'
   sh 'curl https://gist.githubusercontent.com/frnkdny/6ce32d992ec6576548e29312e08fb28b/raw/37252020df292befa7eb99a64da49e/test.log > test.log'
   sh 'pytest'
   } 
}
