node {
   stage('Prepare'){
   echo 'Preparation stage' 
   // inside the container we're root
   sh 'curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python get-pip.py'
   sh 'pip install pytest'
   }
   stage('Test'){
   echo 'Test stage'
   // old test.log url, which had the wrong path towards the end sh 'curl https://gist.githubusercontent.com/frnkdny/6ce32d992ec6576548e29312e08fb28b/raw/37252020df292befa7eb99a64da49e/test.log > test.log'
   // note the last part of the wrong one above ends in  da49e/test.log, the correct one below ends in d63111cc85da49e/test.log
   sh 'curl https://gist.githubusercontent.com/frnkdny/6ce32d992ec6576548e29312e08fb28b/raw/37252020df292befa7eb99a64d63111cc85da49e/test.log > test.log'
   sh 'cp /var/jenkins_home/jobs/Pipelinejob/workspace@script/test_consumeLog.py .'
   // sh 'cp /var/jenkins_home/jobs/Pipelinejob/workspace@script/test.log .'
   sh 'ls -ltra'
   sh 'pytest test_consumeLog.py'
   } 
}
