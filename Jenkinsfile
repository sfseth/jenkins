node {
   stage('Prepare'){
   echo 'Preparation stage' 
   //sh 'sudo yum install -y python-pip && sudo yum install -y pytest'
   sh 'curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python get-pip.py'
   sh 'pip install pytest'
   }
   stage('Test'){
   echo 'Test stage'
   } 
}
