import json,sys
def M(t,topics,lab,w=None,course=None):
    d={'t':t,'topics':topics,'lab':lab}
    if w: d['w']=w
    if course: d['course']=course
    return d
FMT='Live online, one to one'
C=[]
def add(**k):
    k['sessions']=k['weeks']*2
    k['hours']=k['sessions']  # one hour per live session
    C.append(k)

add(slug='linux-networking-scripting',title='Linux, Networking & Scripting',group='Infrastructure',type='short',level='Beginner',weeks=6,
 tagline='The command line, networking and scripting skills every infrastructure role starts from.',
 who=['Career changers moving into IT, cloud or DevOps','Support or admin staff who want to automate their work','Anyone who will take a cloud or DevOps course next'],
 prereq='None. You need a laptop and a stable internet connection.',
 outcomes=['Work confidently in a Linux terminal','Manage users, permissions, packages and services','Explain how IP, DNS, HTTP and TLS fit together','Troubleshoot connectivity with standard tools','Automate repetitive tasks with Bash and Python','Keep your scripts and configuration in Git'],
 modules=[
  M('Linux fundamentals',['Filesystem layout and navigation','Working with files and directories','Searching and filtering text with grep, find and pipes','Editing files with nano and vim','Reading manual pages'],'Organise a messy log directory and find specific errors in it.'),
  M('Users, permissions and processes',['Users, groups and sudo','File permissions with chmod and chown','Processes, signals and job control','Services with systemd','Scheduling with cron'],'Run a small app as a service with a scheduled job.'),
  M('Packages, storage and system health',['Package managers','Disks, partitions and mounts','Reading logs with journalctl','Checking CPU, memory and disk (top, free, df)','Basic performance troubleshooting'],'Diagnose a slow server and write down what you found.'),
  M('Networking essentials',['IP addresses, subnets and CIDR','Ports and protocols','DNS from name to address','HTTP requests and responses','TLS and certificates at a high level'],'Trace a request from a browser to a web server step by step.'),
  M('Network troubleshooting and security basics',['ping, traceroute, curl, dig and ss','Firewalls with ufw and iptables basics','SSH keys and safe remote access','Hardening a server'],'Lock down SSH and open only the ports the server needs.'),
  M('Scripting with Bash and Python',['Variables, loops, functions and exit codes','Reading and writing files','Calling a web API from Python','Git basics: commit, branch, push'],'Build a backup-and-report script and keep it in a Git repository.')],
 tools=['Linux (Ubuntu)','Bash','Python','Git','SSH','systemd'],
 projects=['A server health report script','A hardened Linux server with a service and a scheduled job'],
 prepares=['Linux Essentials (foundation level)'],next=['aws-cloud-computing-ai','docker-cicd-pipelines'])

add(slug='aws-cloud-computing-ai',title='AWS Cloud Computing & AI',group='Cloud engineering',type='short',level='Beginner',weeks=8,
 tagline='Core AWS services, security and architecture, plus a first look at AI services on AWS.',
 who=['Beginners who want to start a cloud career','IT staff moving workloads to AWS','Learners preparing for the AWS Cloud Practitioner exam'],
 prereq='None. Basic computer skills are enough. Linux knowledge helps but is not required.',
 outcomes=['Explain cloud models and the shared responsibility model','Create and secure an AWS account with budgets and alerts','Build a web application on EC2, a load balancer and a VPC','Store data in S3, RDS and DynamoDB','Create least-privilege access with IAM','Build a small serverless API and monitor it with CloudWatch','Use managed AI services in a simple application'],
 modules=[
  M('Cloud concepts and AWS basics',['IaaS, PaaS and SaaS','Shared responsibility model','Regions and Availability Zones','Console and AWS CLI','Billing, free tier and budgets'],'Set up a secured account with budget alerts.'),
  M('Identity and security',['IAM users, groups, roles and policies','Least privilege and MFA','Encryption and KMS basics','Security groups and network ACLs'],'Create least-privilege roles for a small team.'),
  M('Compute and networking',['EC2, AMIs and EBS','Auto Scaling and load balancing','VPC, subnets, routing and NAT','Public and private resources'],'Run a web app behind a load balancer inside a VPC.'),
  M('Storage and databases',['S3 storage classes, versioning and policies','EFS and shared storage','RDS and backups','DynamoDB basics'],'Host a static site on S3 and connect an app to a database.'),
  M('Serverless, monitoring and automation',['Lambda and API Gateway','CloudWatch metrics, logs and alarms','Intro to CloudFormation','Scripting with the AWS CLI'],'Build a serverless API and add alarms for errors.'),
  M('AI on AWS and exam preparation',['Overview of managed AI services, including Amazon Bedrock','Responsible AI basics','Cost optimisation and the Well-Architected pillars','Practice questions and exam review'],'Add a small AI feature to your app with a managed service.')],
 tools=['AWS Console','AWS CLI','EC2','S3','IAM','VPC','RDS','Lambda','CloudWatch'],
 projects=['A secured, load-balanced web application','A serverless API with monitoring'],
 prepares=['AWS Certified Cloud Practitioner'],next=['docker-cicd-pipelines','terraform-ansible'])

add(slug='docker-cicd-pipelines',title='Docker & CI/CD Pipelines',group='DevOps and automation',type='short',level='Beginner to intermediate',weeks=6,
 tagline='Package applications in containers and ship them with automated pipelines.',
 who=['Aspiring DevOps engineers','Developers who want to automate builds and releases','Cloud learners adding a hands-on delivery skill'],
 prereq='Basic Linux command line and Git. The Linux, Networking & Scripting course covers this.',
 outcomes=['Use Git branching and pull requests in a team workflow','Write Dockerfiles and build small, safe images','Run multi-service apps with Docker Compose','Build a CI pipeline with GitHub Actions','Deploy automatically to a server or cloud environment','Use release strategies such as rolling and blue-green','Add tests and security checks to a pipeline'],
 modules=[
  M('Git and collaboration',['Branching strategies','Pull requests and code review','Resolving merge conflicts','Protecting the main branch'],'Practise a pull request workflow on a sample repository.'),
  M('Docker fundamentals',['Images and containers','Writing a Dockerfile','Layers and build caching','Volumes and networks','Registries'],'Containerise a small web application.'),
  M('Compose and image best practice',['Docker Compose for multi-service apps','Configuration and secrets','Small and secure images','Image scanning'],'Run an application with a database using Compose.'),
  M('Continuous integration with GitHub Actions',['Workflows, triggers and runners','Running tests automatically','Caching and artifacts','Secrets in pipelines'],'Build a pipeline that tests and builds on every push.'),
  M('Continuous delivery and release strategies',['Pushing images to a registry','Deploying to a cloud server','Environments and approvals','Rolling, blue-green and canary releases','Rollbacks'],'Deploy to a cloud VM with an approval step.'),
  M('Pipeline quality and capstone',['Linting and security scanning in CI','Reading and fixing pipeline failures','How the same ideas work in Jenkins and GitLab CI','Capstone review'],'Present your complete pipeline from commit to running container.')],
 tools=['Git','GitHub','Docker','Docker Compose','GitHub Actions'],
 projects=['A containerised application with a complete CI/CD pipeline'],
 prepares=[],next=['kubernetes-in-practice','terraform-ansible'])

add(slug='kubernetes-in-practice',title='Kubernetes in Practice',group='DevOps and automation',type='short',level='Intermediate',weeks=6,
 tagline='Deploy, scale and troubleshoot real workloads on Kubernetes.',
 who=['DevOps and cloud engineers running containers','Developers who deploy to Kubernetes','Learners preparing for CKA or CKAD'],
 prereq='Docker basics and a comfortable Linux command line.',
 outcomes=['Explain the Kubernetes architecture','Deploy and update applications with Deployments','Expose apps with Services and Ingress','Manage configuration, secrets and storage','Package apps with Helm','Scale and roll back safely','Troubleshoot failing workloads'],
 modules=[
  M('Architecture and first cluster',['Control plane and nodes','The API server and kubectl','Local clusters with kind or minikube','Objects and YAML manifests'],'Create a local cluster and deploy your first Pod.'),
  M('Workloads',['Pods, ReplicaSets and Deployments','Labels and selectors','Readiness and liveness probes','Resource requests and limits'],'Deploy an app with health checks and resource limits.'),
  M('Networking',['Services: ClusterIP, NodePort and LoadBalancer','Ingress controllers','DNS inside the cluster','NetworkPolicy basics'],'Expose an application through an Ingress.'),
  M('Configuration and storage',['ConfigMaps and Secrets','Volumes, PersistentVolumes and claims','StatefulSets','Backups at a high level'],'Run a database with persistent storage.'),
  M('Packaging and delivery',['Helm charts and values','Kustomize overview','GitOps and Argo CD introduction'],'Package your app as a Helm chart and deploy it with Argo CD.'),
  M('Operations and troubleshooting',['Horizontal Pod Autoscaler','Rolling updates and rollbacks','RBAC basics','Debugging with describe, logs and events','Managed Kubernetes such as EKS'],'Fix a set of broken deployments against the clock.')],
 tools=['Kubernetes','kubectl','Helm','kind','Argo CD'],
 projects=['A Helm-packaged application with autoscaling and a GitOps deployment'],
 prepares=['A good base for the CKA and CKAD exams'],next=['monitoring-observability','devops-engineer-program'])

add(slug='terraform-ansible',title='Terraform & Ansible',group='Infrastructure',type='short',level='Intermediate',weeks=6,
 tagline='Provision and configure infrastructure as version-controlled code.',
 who=['DevOps and cloud engineers','System administrators moving to automation','Learners preparing for the Terraform Associate exam'],
 prereq='Linux basics and some AWS experience, for example the AWS Cloud Computing & AI course.',
 outcomes=['Explain infrastructure as code and why it matters','Write Terraform for networks, servers and load balancers','Organise code with variables, outputs and modules','Manage state safely in a team','Configure servers repeatably with Ansible playbooks','Combine Terraform and Ansible in one workflow'],
 modules=[
  M('Infrastructure as code and Terraform basics',['Declarative infrastructure','Providers and resources','plan, apply and destroy','What state is and why it matters'],'Create and destroy your first cloud resources with code.'),
  M('Variables, outputs and modules',['Input variables and locals','Outputs','Writing reusable modules','Using registry modules'],'Build a reusable network module.'),
  M('State and working in teams',['Remote state with locking','Environments and workspaces','Detecting and handling drift','Importing existing resources'],'Move state to a remote backend and share it with a teammate.'),
  M('Terraform on AWS',['VPC, subnets and security groups','EC2 and load balancers','IAM roles for infrastructure','fmt, validate and plan in CI'],'Deploy a three-tier layout with code.'),
  M('Ansible fundamentals',['Inventory and ad-hoc commands','Playbooks and modules','Variables, handlers and idempotence','Testing playbooks'],'Configure a group of web servers with one playbook.'),
  M('Roles and a combined workflow',['Roles and Jinja2 templates','Ansible Vault for secrets','Terraform creates, Ansible configures','Capstone review'],'Provision servers with Terraform and configure them with Ansible.')],
 tools=['Terraform','Ansible','AWS','Git'],
 projects=['A complete environment provisioned and configured from code'],
 prepares=['HashiCorp Certified: Terraform Associate'],next=['kubernetes-in-practice','devops-engineer-program'])

add(slug='monitoring-observability',title='Monitoring & Observability',group='Reliability and SRE',type='short',level='Intermediate',weeks=4,
 tagline='See what your systems are doing with metrics, dashboards, alerts, logs and traces.',
 who=['DevOps and SRE engineers','Developers who run their own services','Operations staff who handle alerts'],
 prereq='Linux basics and some container experience.',
 outcomes=['Choose useful signals for a service','Collect metrics with Prometheus','Build Grafana dashboards','Write alerts that are actionable and route them well','Search logs and follow a request with traces','Connect metrics, logs and traces during an investigation'],
 modules=[
  M('Observability foundations',['Monitoring and observability compared','Metrics, logs and traces','The four golden signals','RED and USE methods'],'Pick the right signals for a sample service.'),
  M('Metrics with Prometheus',['How scraping works','Exporters and instrumentation','PromQL basics','Recording rules'],'Instrument an app and query its metrics.'),
  M('Dashboards and alerts',['Grafana dashboards and variables','Alert rules and Alertmanager routing','Avoiding alert fatigue','Writing runbook links into alerts'],'Build a dashboard and an alert that pages the right person.'),
  M('Logs, traces and capstone',['Centralised logging with Loki or the ELK stack','Tracing and OpenTelemetry overview','Correlating signals during an incident','Capstone review'],'Set up the full stack for a sample application.')],
 tools=['Prometheus','Grafana','Alertmanager','OpenTelemetry','Loki'],
 projects=['A monitoring stack with dashboards and alerts for a sample application'],
 prepares=[],next=['sre-essentials','sre-program'])

add(slug='sre-essentials',title='SRE Essentials',group='Reliability and SRE',type='short',level='Intermediate',weeks=5,
 tagline='SLOs, error budgets, incident response and the habits of reliable teams.',
 who=['Engineers moving towards SRE roles','DevOps engineers who own production systems','Team leads who want a reliability practice'],
 prereq='Linux basics. Some cloud or container experience helps.',
 outcomes=['Explain what SRE is and how it differs from DevOps','Define SLIs, SLOs and error budgets for a service','Set up burn-rate style alerts','Run an incident with clear roles and communication','Write a blameless postmortem','Reduce toil with automation'],
 modules=[
  M('SRE principles',['SRE and DevOps compared','Toil and how to measure it','Reliability as a feature','Risk and trade-offs'],'Audit the toil in a sample team.'),
  M('SLIs, SLOs and error budgets',['Choosing good SLIs','Setting targets with users in mind','Error budgets and policies','Burn-rate alerting'],'Define SLOs for a sample service.'),
  M('Incident response',['Roles, severity levels and on-call','Communication during incidents','Runbooks and escalation','Mitigate first, investigate second'],'Take part in a simulated incident.'),
  M('Postmortems and learning',['Blameless culture','Timelines and contributing factors','Useful action items','Sharing what you learned'],'Write the postmortem for your simulated incident.'),
  M('Reliability engineering practice',['Capacity planning and load testing','Redundancy and graceful degradation','Intro to chaos engineering','Automating away toil'],'Review the reliability of a system design.')],
 tools=['Prometheus','Grafana','Runbooks','Incident tooling'],
 projects=['An SLO document, a runbook and a postmortem for a simulated incident'],
 prepares=[],next=['monitoring-observability','sre-program'])

add(slug='devops-engineer-program',title='DevOps Engineer Program',group='DevOps and automation',type='long',level='Beginner to job-ready',weeks=36,
 tagline='The full path from Linux basics to a job-ready DevOps portfolio, with a coach all the way.',
 who=['Career changers aiming for a DevOps engineer role','IT professionals who want a structured path','Developers moving into platform and delivery work'],
 prereq='None. Beginners are welcome. Your coach adjusts the pace to your background.',
 outcomes=['Work confidently with Linux, networking and scripting','Build and secure infrastructure on AWS','Containerise applications and automate delivery with CI/CD','Run workloads on Kubernetes','Define environments with Terraform and Ansible','Add monitoring and alerts to what you build','Present a portfolio project, CV and interview answers'],
 modules=[
  M('Linux, networking and scripting',['The command line and permissions','Networking and troubleshooting','Bash, Python and Git'],'Covered in the Linux, Networking & Scripting course.',w=6,course='linux-networking-scripting'),
  M('Cloud on AWS',['IAM and security','Compute, networking and storage','Serverless and monitoring'],'Covered in the AWS Cloud Computing & AI course.',w=8,course='aws-cloud-computing-ai'),
  M('Containers and CI/CD',['Docker and Compose','GitHub Actions pipelines','Release strategies'],'Covered in the Docker & CI/CD Pipelines course.',w=6,course='docker-cicd-pipelines'),
  M('Kubernetes',['Workloads, networking and storage','Helm and GitOps','Operations and troubleshooting'],'Covered in the Kubernetes in Practice course.',w=6,course='kubernetes-in-practice'),
  M('Infrastructure as code',['Terraform on AWS','State and modules','Ansible configuration'],'Covered in the Terraform & Ansible course.',w=6,course='terraform-ansible'),
  M('Capstone and career preparation',['Design and build an end-to-end project: app, pipeline, infrastructure code, Kubernetes and monitoring','Portfolio and GitHub profile','CV and LinkedIn review','Mock interviews and feedback'],'Present your capstone project and answer interview-style questions about it.',w=4)],
 tools=['Linux','Git','AWS','Docker','GitHub Actions','Kubernetes','Helm','Terraform','Ansible','Prometheus','Grafana'],
 projects=['An end-to-end capstone: application, CI/CD pipeline, Terraform-built infrastructure, Kubernetes deployment and monitoring'],
 prepares=['AWS Certified Cloud Practitioner','HashiCorp Certified: Terraform Associate','A good base for the CKA and CKAD exams'],next=['sre-program'])

add(slug='sre-program',title='Site Reliability Engineer Program',group='Reliability and SRE',type='long',level='Beginner to job-ready',weeks=33,
 tagline='The full path to an SRE role, with hands-on incident practice.',
 who=['Career changers aiming for an SRE role','DevOps and operations engineers moving to SRE','Developers who want to own reliability'],
 prereq='None. Beginners are welcome. Your coach adjusts the pace to your background.',
 outcomes=['Work confidently with Linux, networking and scripting','Run and secure workloads on AWS and Kubernetes','Build monitoring, dashboards and alerts','Define SLOs and manage error budgets','Lead an incident and write a blameless postmortem','Show a reliability project in your portfolio'],
 modules=[
  M('Linux, networking and scripting',['The command line and permissions','Networking and troubleshooting','Bash, Python and Git'],'Covered in the Linux, Networking & Scripting course.',w=6,course='linux-networking-scripting'),
  M('Cloud on AWS',['IAM and security','Compute, networking and storage','Serverless and monitoring'],'Covered in the AWS Cloud Computing & AI course.',w=8,course='aws-cloud-computing-ai'),
  M('Monitoring and observability',['Prometheus and Grafana','Alerting that works','Logs and traces'],'Covered in the Monitoring & Observability course.',w=4,course='monitoring-observability'),
  M('SRE essentials',['SLIs, SLOs and error budgets','Incident response','Postmortems and toil'],'Covered in the SRE Essentials course.',w=5,course='sre-essentials'),
  M('Kubernetes',['Workloads, networking and storage','Operations and troubleshooting','Autoscaling and rollbacks'],'Covered in the Kubernetes in Practice course.',w=6,course='kubernetes-in-practice'),
  M('Capstone and career preparation',['A reliability project: define SLOs, instrument a service, set up alerts, run a game day and write a postmortem','Portfolio and GitHub profile','CV and LinkedIn review','Mock interviews and feedback'],'Present your reliability project and answer interview-style questions about it.',w=4)],
 tools=['Linux','Git','AWS','Kubernetes','Prometheus','Grafana','Alertmanager','Runbooks'],
 projects=['A reliability capstone: SLOs, monitoring, alerting, a game day and a written postmortem'],
 prepares=['AWS Certified Cloud Practitioner','A good base for the CKA and CKAD exams'],next=['devops-engineer-program'])

add(slug='aws-cloud-engineering-ai',title='AWS Cloud Engineering & AI',group='Cloud engineering',type='long',level='Beginner to job-ready',weeks=40,
 tagline='Build, automate and run cloud infrastructure on AWS, with applied AI, in an extended program.',
 who=['Career changers aiming for a cloud engineer role','IT professionals moving to the cloud','Learners who want AWS certifications and a portfolio'],
 prereq='None. Beginners are welcome. Your coach adjusts the pace to your background.',
 outcomes=['Work confidently with Linux, Python and SQL','Design secure, resilient architectures on AWS','Run containers on ECS and understand EKS','Build environments with Terraform','Deploy to AWS with CI/CD and monitor with CloudWatch','Build a small AI-powered application with managed AWS services','Present a final project, CV and interview answers'],
 modules=[
  M('Foundations: Linux, Python and SQL',['The Linux command line and networking','Python scripting and Git','SQL and relational database basics'],'Write a script that reads data, stores it in a database and reports on it.',w=6),
  M('AWS core services',['IAM and security','EC2, VPC, S3 and databases','Serverless and CloudWatch'],'Covered in the AWS Cloud Computing & AI course.',w=8,course='aws-cloud-computing-ai'),
  M('Architecture, security and cost',['The Well-Architected Framework','Multi-AZ and highly available designs','VPC design: endpoints and peering','Advanced IAM, encryption and logging with CloudTrail and Config','Cost optimisation'],'Design and deploy a resilient three-tier architecture.',w=6),
  M('Containers on AWS',['Docker and image registries','ECR and ECS with Fargate','Overview of EKS'],'Deploy a containerised application to ECS.',w=5),
  M('Infrastructure as code',['Terraform on AWS','State, modules and environments','Pipeline checks for infrastructure code'],'Rebuild your architecture project entirely with Terraform.',w=5),
  M('CI/CD and observability',['GitHub Actions deploying to AWS','CloudWatch dashboards and alarms','Prometheus and Grafana basics'],'Ship changes to AWS automatically and watch them with dashboards.',w=5),
  M('AI on AWS',['Managed AI services and Amazon Bedrock','Building a small AI-powered application','Responsible AI','AWS AI Practitioner exam preparation'],'Build and deploy an AI-powered feature on AWS.',w=3),
  M('Final project and career preparation',['Plan and present a final project','Portfolio and GitHub profile','CV and LinkedIn review','Mock interviews and feedback'],'Present your final project and answer interview-style questions about it.',w=2)],
 tools=['Linux','Python','SQL','AWS','Docker','ECS','Terraform','GitHub Actions','CloudWatch','Amazon Bedrock'],
 projects=['A resilient three-tier architecture built with Terraform','An AI-powered application deployed on AWS','A final project presented to your coach'],
 prepares=['AWS Certified Cloud Practitioner','AWS Certified AI Practitioner','AWS Certified Solutions Architect - Associate','HashiCorp Certified: Terraform Associate'],next=['devops-engineer-program'])

add(slug='azure-cloud-computing',title='Azure Cloud Computing',group='Azure cloud',type='short',level='Beginner',weeks=8,
 tagline='Core Azure services, identity, networking and governance, ending with AZ-900 preparation.',
 who=['Beginners starting a cloud career on Microsoft Azure','IT staff moving workloads from on-premises Windows or Linux to Azure','Learners preparing for the AZ-900 exam'],
 prereq='None. Basic computer skills are enough.',
 outcomes=['Explain cloud models and the shared responsibility model','Create and organise Azure subscriptions, resource groups and budgets','Deploy virtual machines and web apps and put them behind a load balancer','Design a virtual network with subnets and security groups','Store data in Blob Storage and Azure SQL','Control access with Microsoft Entra ID and role-based access control','Monitor resources and set up alerts'],
 modules=[
  M('Cloud concepts and Azure basics',['IaaS, PaaS and SaaS','Shared responsibility model','Regions and availability zones','Azure portal and Azure CLI','Subscriptions, resource groups and cost management'],'Set up a subscription with budgets and a sensible resource group layout.'),
  M('Identity and access',['Microsoft Entra ID basics','Users, groups and role-based access control','Least privilege and MFA','Conditional access at a high level'],'Give a small team the minimum access they need.'),
  M('Compute',['Virtual machines and disks','Scale sets and availability sets','App Service','Containers in Azure at a high level'],'Deploy a web app on a virtual machine and again on App Service.'),
  M('Networking',['Virtual networks, subnets and peering','Network security groups','Load balancer and Application Gateway','DNS and VPN at a high level'],'Build a two-tier network with a public front end and a private back end.'),
  M('Storage and databases',['Blob, file and disk storage','Redundancy options','Azure SQL Database','Backups and recovery'],'Host a static site in Blob Storage and connect an app to a database.'),
  M('Governance, monitoring and exam preparation',['Azure Policy and resource locks','Azure Monitor and alerts','Pricing and the Well-Architected Framework','Practice questions and AZ-900 review'],'Add alerts to your app and review its cost.')],
 tools=['Azure portal','Azure CLI','Virtual Machines','App Service','Blob Storage','Azure SQL','Microsoft Entra ID','Azure Monitor'],
 projects=['A secured, load-balanced web application on Azure','A governed subscription with budgets, policy and alerts'],
 prepares=['Microsoft Azure Fundamentals (AZ-900)'],next=['azure-administrator','docker-cicd-pipelines'])

add(slug='azure-administrator',title='Azure Administrator',group='Azure cloud',type='short',level='Intermediate',weeks=8,
 tagline='Run Azure day to day: identity, networks, compute, storage, backups and monitoring, ending with AZ-104 preparation.',
 who=['Cloud and systems administrators working with Azure','Learners who finished Azure Cloud Computing','Engineers preparing for the AZ-104 exam'],
 prereq='Basic Azure knowledge, such as the Azure Cloud Computing course, and Linux or Windows administration basics.',
 outcomes=['Manage identities, groups and role assignments at scale','Configure virtual networks, peering, DNS and secure access','Deploy and resize virtual machines and scale sets','Manage storage accounts, access and lifecycle rules','Run containers on App Service and Azure Container Apps','Back up and restore workloads','Monitor with Azure Monitor and Log Analytics and act on alerts'],
 modules=[
  M('Identities and governance',['Entra ID users, groups and devices','Role-based access control in depth','Management groups, policy and tags','Cost management and budgets'],'Design the access and policy model for a three-team subscription.'),
  M('Virtual networking',['Virtual networks, subnets and routing','Network security groups and Azure Firewall basics','Peering and VPN gateways','Private endpoints and DNS'],'Connect two networks and restrict traffic between them.'),
  M('Virtual machines',['Images, sizes and disks','Scale sets and autoscaling','Availability and update management','Access with Bastion and managed identities'],'Deploy a scale set that grows and shrinks with load.'),
  M('Storage',['Storage accounts and redundancy','Shared access signatures and keys','Lifecycle management','Azure Files and sync'],'Secure a storage account and automate its lifecycle.'),
  M('Containers and web apps',['App Service plans and slots','Azure Container Registry','Azure Container Apps','Deployment slots and rollbacks'],'Deploy a containerised app with a staging slot swap.'),
  M('Backup, monitoring and exam preparation',['Azure Backup and recovery vaults','Azure Monitor, Log Analytics and alerts','Automating tasks with Azure CLI and ARM or Bicep templates','Practice questions and AZ-104 review'],'Restore a deleted machine from backup and alert on failures.')],
 tools=['Azure CLI','Microsoft Entra ID','Virtual Networks','Virtual Machines','Storage Accounts','App Service','Azure Monitor','Bicep'],
 projects=['A governed, monitored multi-tier environment on Azure','A backup and restore runbook'],
 prepares=['Microsoft Azure Administrator Associate (AZ-104)'],next=['terraform-ansible','kubernetes-in-practice'])

add(slug='google-cloud-computing',title='Google Cloud Computing',group='Google Cloud',type='short',level='Beginner',weeks=8,
 tagline='Core Google Cloud services, IAM, networking and data, with a first look at AI and Cloud Digital Leader preparation.',
 who=['Beginners starting a cloud career on Google Cloud','Developers and analysts moving workloads to Google Cloud','Learners preparing for the Cloud Digital Leader exam'],
 prereq='None. Basic computer skills are enough.',
 outcomes=['Explain cloud models and how Google Cloud is organised','Create projects, billing budgets and alerts','Run applications on Compute Engine, Cloud Run and App Engine','Create secure access with IAM and service accounts','Design a VPC network with firewall rules','Store data in Cloud Storage, Cloud SQL and BigQuery','Use managed AI services in a simple application'],
 modules=[
  M('Cloud concepts and Google Cloud basics',['IaaS, PaaS and SaaS','Organisation, folders and projects','Regions and zones','Console, Cloud Shell and the gcloud CLI','Billing and budgets'],'Set up a project with a budget alert.'),
  M('Identity and security',['IAM roles and policies','Service accounts','Least privilege and MFA','Encryption and Cloud KMS basics'],'Give a team and an application only the access they need.'),
  M('Compute',['Compute Engine and persistent disks','Managed instance groups and load balancing','Cloud Run and App Engine','Containers on Google Cloud at a high level'],'Deploy the same app on a VM and on Cloud Run and compare them.'),
  M('Networking',['VPC networks and subnets','Firewall rules','Cloud DNS and Cloud Load Balancing','Hybrid connectivity at a high level'],'Build a VPC with public and private workloads.'),
  M('Storage, data and AI',['Cloud Storage classes and lifecycle','Cloud SQL','BigQuery basics','Vertex AI and managed AI services at a high level'],'Load data into BigQuery and query it.'),
  M('Operations and exam preparation',['Cloud Monitoring and Logging','Pricing and cost control','Digital transformation concepts','Practice questions and Cloud Digital Leader review'],'Set up dashboards and alerts for your app.')],
 tools=['Google Cloud console','gcloud CLI','Compute Engine','Cloud Run','Cloud Storage','BigQuery','IAM','Cloud Monitoring'],
 projects=['A secured web application on Google Cloud','A small data analysis in BigQuery'],
 prepares=['Google Cloud Digital Leader'],next=['google-cloud-engineer','docker-cicd-pipelines'])

add(slug='google-cloud-engineer',title='Google Cloud Engineer',group='Google Cloud',type='short',level='Intermediate',weeks=8,
 tagline='Deploy, secure and operate workloads on Google Cloud, ending with Associate Cloud Engineer preparation.',
 who=['Engineers working on or moving to Google Cloud','Learners who finished Google Cloud Computing','Candidates preparing for the Associate Cloud Engineer exam'],
 prereq='Basic Google Cloud knowledge, such as the Google Cloud Computing course, and Linux command line basics.',
 outcomes=['Plan projects, billing and IAM for a team','Deploy and scale applications on Compute Engine, Cloud Run and GKE','Build and secure VPC networks across projects','Choose between storage and database options','Automate deployments with gcloud and Terraform','Monitor, log and alert on workloads','Troubleshoot common deployment problems'],
 modules=[
  M('Projects, billing and access',['Resource hierarchy and organisation policies','IAM, groups and service account best practice','Budgets and quotas','Audit logs'],'Design the project and access layout for a small company.'),
  M('Compute and containers',['Compute Engine templates and instance groups','Cloud Run revisions and traffic splitting','Google Kubernetes Engine fundamentals','Artifact Registry'],'Deploy an app on Cloud Run and on GKE.'),
  M('Networking',['VPC design, shared VPC and peering','Firewall rules and Cloud NAT','Load balancing options','Private Google access'],'Build a private network with controlled outbound access.'),
  M('Storage and databases',['Cloud Storage security and lifecycle','Cloud SQL, Firestore and Spanner at a glance','BigQuery access and cost control','Backups and exports'],'Pick the right database for three sample applications and justify it.'),
  M('Automation and delivery',['gcloud scripting','Terraform on Google Cloud','Cloud Build pipelines','Deployment rollbacks'],'Provision an environment with Terraform and deploy it with Cloud Build.'),
  M('Operations and exam preparation',['Cloud Monitoring, Logging and alerting','Troubleshooting deployments and permissions','Cost optimisation','Practice questions and Associate Cloud Engineer review'],'Find and fix three planted problems in a broken environment.')],
 tools=['gcloud CLI','Compute Engine','Cloud Run','GKE','Cloud Build','Terraform','Cloud Monitoring','BigQuery'],
 projects=['A containerised application delivered with Cloud Build','An environment defined with Terraform'],
 prepares=['Google Cloud Associate Cloud Engineer'],next=['kubernetes-in-practice','terraform-ansible'])

add(slug='aws-solutions-architect',title='AWS Solutions Architect',group='AWS cloud',type='short',level='Intermediate',weeks=8,
 tagline='Design secure, resilient, cost-aware architectures on AWS, ending with Solutions Architect Associate preparation.',
 who=['Engineers who finished AWS Cloud Computing & AI','Developers and administrators designing systems on AWS','Candidates preparing for the Solutions Architect Associate exam'],
 prereq='Basic AWS knowledge, such as the AWS Cloud Computing & AI course.',
 outcomes=['Design highly available and fault-tolerant architectures','Choose the right compute, storage and database services','Design secure networks and access across accounts','Decouple applications with queues, topics and event buses','Plan backup, recovery and disaster recovery','Estimate and reduce cost','Review a design against the Well-Architected Framework'],
 modules=[
  M('Resilient architecture',['Multi-AZ and multi-region patterns','Load balancing and Auto Scaling','Decoupling with SQS, SNS and EventBridge','Disaster recovery strategies'],'Make a single-server app survive the loss of an Availability Zone.'),
  M('Secure architecture',['IAM across accounts and AWS Organizations','Network security: security groups, NACLs and endpoints','Encryption with KMS and Secrets Manager','Logging with CloudTrail and Config'],'Lock down a multi-account setup.'),
  M('Compute and containers',['EC2 purchasing options','Lambda patterns','ECS and Fargate overview','Choosing between them'],'Compare three compute choices for the same workload.'),
  M('Storage and databases',['S3 design and performance','Block and file storage','RDS, Aurora and DynamoDB design','Caching with ElastiCache and CloudFront'],'Choose and justify the data layer for three applications.'),
  M('Performance and cost',['Right-sizing and savings plans','Cost Explorer and budgets','Performance monitoring','Trade-offs between cost, speed and resilience'],'Cut the monthly cost of a sample architecture without lowering availability.'),
  M('Design practice and exam preparation',['Reading exam-style scenarios','Well-Architected review','Whiteboard a design and defend it','Practice questions and exam review'],'Present an architecture and answer questions on it.')],
 tools=['EC2','S3','VPC','RDS and Aurora','DynamoDB','SQS and SNS','CloudFront','CloudTrail'],
 projects=['A multi-AZ architecture with a written design review','A disaster recovery plan for a sample application'],
 prepares=['AWS Certified Solutions Architect - Associate'],next=['terraform-ansible','aws-cloud-engineering-ai'])

add(slug='python-for-devops',title='Python for DevOps',group='DevOps and automation',type='short',level='Beginner to intermediate',weeks=5,
 tagline='Use Python to automate infrastructure, call cloud APIs and build small operations tools.',
 who=['Aspiring DevOps and cloud engineers','System administrators moving from Bash to Python','Anyone who wants to automate cloud work'],
 prereq='Basic Linux command line. Programming experience is not needed.',
 outcomes=['Write clear Python scripts with functions and error handling','Work with files, JSON and YAML','Call REST APIs and handle responses','Automate AWS, Azure or Google Cloud tasks with their Python libraries','Write tests for your scripts','Package a tool others can run'],
 modules=[
  M('Python essentials',['Variables, loops and functions','Virtual environments and pip','Reading and writing files','Errors and logging'],'Write a script that cleans and summarises a log file.'),
  M('Data formats and APIs',['JSON and YAML','The requests library','Authentication and pagination','Retries and timeouts'],'Pull data from a public API and produce a report.'),
  M('Automating the cloud',['Cloud SDKs: boto3 and equivalents','Listing and tagging resources','Scheduled clean-up of unused resources','Handling credentials safely'],'Write a tool that finds and reports untagged cloud resources.'),
  M('Testing and quality',['Unit tests with pytest','Linting and formatting','Running tests in CI','Command line interfaces with argparse'],'Add tests and a CI check to your tool.'),
  M('Operations tools',['Small web services with Flask or FastAPI','Health checks and webhooks','Packaging and releasing a tool','Capstone review'],'Present a working operations tool and explain how it is tested.')],
 tools=['Python','pytest','Git','GitHub Actions','REST APIs','boto3'],
 projects=['A cloud resource report tool with tests','A small health-check service'],
 prepares=[],next=['docker-cicd-pipelines','terraform-ansible'])

add(slug='jenkins-gitlab-ci',title='CI/CD with Jenkins & GitLab CI',group='DevOps and automation',type='short',level='Intermediate',weeks=5,
 tagline='Build and run pipelines in the two CI/CD systems most teams still use.',
 who=['DevOps engineers who work in teams that use Jenkins or GitLab','Learners who finished Docker & CI/CD Pipelines','Engineers moving between CI/CD tools'],
 prereq='Docker and Git basics, such as the Docker & CI/CD Pipelines course.',
 outcomes=['Install and secure a Jenkins server','Write declarative Jenkins pipelines with a Jenkinsfile','Use agents, credentials and shared libraries','Write GitLab CI pipelines with stages, jobs and runners','Build, test and publish container images in both tools','Deploy with approvals and rollbacks','Choose between GitHub Actions, Jenkins and GitLab CI'],
 modules=[
  M('Jenkins fundamentals',['Installing Jenkins and plugins','Users, roles and security','Jobs and pipelines','Agents and nodes'],'Run Jenkins in a container and secure it.'),
  M('Jenkins pipelines',['Declarative Jenkinsfile','Credentials and secrets','Shared libraries','Webhooks and multibranch pipelines'],'Write a Jenkinsfile that builds, tests and publishes an image.'),
  M('GitLab CI fundamentals',['.gitlab-ci.yml, stages and jobs','Runners and variables','Artifacts and caching','Merge request pipelines'],'Build a pipeline that tests every merge request.'),
  M('Delivery and deployment',['Container registry','Environments and manual approvals','Review apps and rollbacks','Deploying to Kubernetes or a cloud server'],'Deploy to a staging and a production environment with an approval step.'),
  M('Comparing tools and capstone',['Strengths and limits of each tool','Migrating a pipeline between tools','Pipeline security and speed','Capstone review'],'Rebuild the same pipeline in two tools and compare the results.')],
 tools=['Jenkins','GitLab CI','Docker','Git','Kubernetes','Container registries'],
 projects=['The same application delivered through Jenkins and through GitLab CI'],
 prepares=[],next=['kubernetes-in-practice','devsecops-essentials'])

add(slug='devsecops-essentials',title='DevSecOps Essentials',group='DevOps and automation',type='short',level='Intermediate',weeks=5,
 tagline='Build security into pipelines, containers, infrastructure code and cloud accounts.',
 who=['DevOps and cloud engineers who need to ship securely','Developers adding security checks to their delivery process','Learners who finished a CI/CD course'],
 prereq='Docker and CI/CD basics, such as the Docker & CI/CD Pipelines course.',
 outcomes=['Explain where security fits across the delivery lifecycle','Scan code, dependencies and container images in a pipeline','Manage secrets without putting them in code','Check infrastructure code for risky settings','Apply least privilege in cloud accounts and Kubernetes','Respond to a vulnerability report with a clear process'],
 modules=[
  M('Security in the delivery lifecycle',['Shift-left security','Threat modelling basics','The OWASP Top 10 at a high level','Security responsibilities in a team'],'Threat-model a small web application.'),
  M('Code and dependency security',['Static analysis (SAST)','Dependency and licence scanning','Software bills of materials','Fixing findings without slowing delivery'],'Add code and dependency scanning to a pipeline.'),
  M('Container and secrets security',['Image scanning and hardening','Running as non-root','Secrets managers and rotation','Signing images'],'Harden a container image and move its secrets to a manager.'),
  M('Infrastructure and cloud security',['Scanning Terraform and Kubernetes files','Least-privilege IAM','Network policy basics','Audit logging'],'Find and fix risky settings in a sample Terraform project.'),
  M('Operating securely',['Vulnerability management process','Incident response basics','Security metrics','Capstone review'],'Handle a simulated vulnerability report from alert to fix.')],
 tools=['Trivy','Semgrep','Gitleaks','Docker','Terraform','GitHub Actions','Vault or cloud secrets managers'],
 projects=['A pipeline that scans code, dependencies, images and infrastructure files'],
 prepares=[],next=['kubernetes-in-practice','sre-essentials'])

add(slug='gitops-helm-argocd',title='GitOps with Helm & Argo CD',group='DevOps and automation',type='short',level='Intermediate',weeks=4,
 tagline='Package applications with Helm and deliver them to Kubernetes from Git with Argo CD.',
 who=['Engineers who already run applications on Kubernetes','Learners who finished Kubernetes in Practice','Platform and DevOps engineers moving to GitOps'],
 prereq='Kubernetes basics, such as the Kubernetes in Practice course.',
 outcomes=['Explain the GitOps model and its benefits','Package an application as a Helm chart','Manage values for several environments','Install and use Argo CD','Deploy, sync and roll back applications from Git','Handle secrets in a GitOps workflow'],
 modules=[
  M('GitOps principles',['Declarative and versioned delivery','Pull versus push deployments','Repository layout for apps and environments','Drift and reconciliation'],'Design a repository layout for three environments.'),
  M('Helm',['Charts, templates and values','Dependencies','Releases and upgrades','Testing and linting charts'],'Package an application as a Helm chart.'),
  M('Argo CD',['Installing and securing Argo CD','Applications and sync policies','Health, drift and rollbacks','App of apps and ApplicationSets'],'Deploy your chart to a cluster from a Git repository.'),
  M('Environments, secrets and capstone',['Promoting between environments','Sealed Secrets or External Secrets','Progressive delivery at a high level','Capstone review'],'Promote a change from development to production through Git only.')],
 tools=['Kubernetes','Helm','Argo CD','Git','GitHub'],
 projects=['An application delivered to three environments through Argo CD'],
 prepares=[],next=['sre-essentials','devops-engineer-program'])

# checks
slugs={c['slug'] for c in C}
for c in C:
    for n in c['next']: assert n in slugs,(c['slug'],n)
    for m in c['modules']:
        if m.get('course'): assert m['course'] in slugs
    ws=[m.get('w') for m in c['modules']]
    if c['type']=='long': assert sum(ws)==c['weeks'],(c['slug'],sum(ws),c['weeks'])
    else: assert len(c['modules'])>=4
json.dump(C,open(sys.argv[1],'w'),ensure_ascii=False,indent=1)
print(len(C),'courses',sum(len(c['modules']) for c in C),'modules')
