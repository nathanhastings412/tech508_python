## Day 2

### Consolidation questions
- What is the cloud?
  - centrally managed
  - delivered as a service over the internet
  - available on demand
- is running things in the cloud always better security?
  - partly - yes because the data is extremely secure, but you do not have access to the physical hardware
  - you do not know who has access to the physical hardware
- can you get into a private cloud system from the outside?
  - no
- Different types of services
  - on premises - you have maximal control and maximal responsibility
  - IaaS - gives you quite a bit to manage but more control, you have access to everything but the infrastructure
  - PaaS - you have less control and therefore fewer responsibilities - your code has to be secure
  - SaaS - you just manage the data and everything else falls on the cloud service provider
- what is a hybrid cloud model?
  - a mix of private(on-prem) and public cloud services (a database might be on prem)

### Interview stuff
- Why do you want to be a support engineer
  - I have had one or two technical issues in the past (be specific)
  - I found a fair amount of satisfaction in troubleshooting and diagnosing the problem and the successfully resolving the problem
  - This opportunity arose
- what is your greatest weakness?
  - nervousness?
	- face the music
	- try to get out of your comfort zone at times
	- there are times where you can override it to an extent
  - properly engaging, sometimes if im nervous i can get distracted thinking about the impression im creating 
  

### stop folder from being included in git repo
- git command `ls -a` shows the hidden folder
- if a folder is already being tracked by git, and then you ignore it, it will still be in the github repo
- this folder will still be visible in previous commits but will not be visible in future commits

### SSH
- we have been using HTTPS to authenticate and push to github
- can also use SSH to securely authenticate and push to github
1. Create SSH key
  - SSH key pair (type: RSA)
    - private version of the key (key)
    - public version of the key (padlock)
      - NOTE: asymmetric - you can generate the public key if you have the private key but not vice versa
2. Register the public key
3. Add private key to the SSH register
4. Create test repo
5. Push changes to the repo using SSH




