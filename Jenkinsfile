node {
   stage('Prepare'){
   echo 'Preparation stage' 
   // inside the container we're root
   sh 'curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python get-pip.py'
   sh 'pip install pytest'
   }
   stage('Test'){
   echo 'Test stage'
   // strangely i started getting 404s from the following url, though it worked earlier, going to use stashed copy for the time being:
   // -rw-rw-r-- 1 ec2-user ec2-user  5453 Nov  8 21:35 test.log
   //sh 'curl https://gist.githubusercontent.com/frnkdny/6ce32d992ec6576548e29312e08fb28b/raw/37252020df292befa7eb99a64da49e/test.log > test.log'
   sh 'cp /var/jenkins_home/jobs/Pipelinejob/workspace@script/test_consumeLog.py .'
   sh 'cp /var/jenkins_home/jobs/Pipelinejob/workspace@script/test.log .'
   sh 'ls -ltra'
   sh 'pytest test_consumeLog.py'
   } 
}
