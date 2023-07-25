# Getting Started LIVOX-AVIA
This repository serves as a comprehensive guide on utilizing the LIVOX-AVIA LiDAR system, covering detailed instructions on its usage, accessing recorded data, and subsequently employing the data for object detection purposes.

## LIVOX Viewer
Upon connecting the LiDAR to the power source and ethernet, the initial step involves modifying the computer's IP address. Access the network settings of the computer and configure the IPv4 address to

``` shell
IP : 192.168.1.5
Subnet Mask : 255.255.255.0
```
Subsequently, to visualize the point clouds, we can make use of the LIVOX-Viewer tool, which is provided by Livox Tech. This software allows us to view and analyze the captured point cloud data from the LIVOX-AVIA LiDAR system.
Download the Livox-Viewer version 0.10 or 0.11 from the following link.
```shell
https://www.livoxtech.com/downloads
```
Once you have downloaded the LIVOX-Viewer software, extract the files from the downloaded package. After extraction, navigate to the folder where the LIVOX-Viewer is located. In this folder, you will find the executable or application file that you can run to launch the LIVOX-Viewer interface. This interface will enable you to interact with and visualize the point cloud data recorded by the LIVOX-AVIA LiDAR.

Run the livox viewer by running :
```shell
./livox_viewer.sh
```
Upon opening the LIVOX-Viewer, you will be able to see the list of available LIVOX LiDAR devices. Once your LIVOX-AVIA LiDAR is connected and recognized by the viewer, it will appear in the list. To observe the point clouds in real-time, simply click on the "play" button provided within the LIVOX-Viewer interface. This action will initiate the visualization of live point cloud data captured by the LIVOX-AVIA LiDAR in real-time.


