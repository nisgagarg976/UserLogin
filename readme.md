# Installing Ubuntu

## Download Ubuntu ISO Image

1. Go to the [official Ubuntu website](https://ubuntu.com/download) and download the desired version of Ubuntu.

## Create Bootable USB Drive.schema TABLENAME


1. Insert a USB drive with sufficient storage capacity (at least 4GB).
2. create a bootabke usb from startup disk creator .
3. Open the tool and select the Ubuntu ISO file you downloaded.
4. Choose the USB drive as the destination.
5. Click on "Start" or "Flash" to create the bootable USB drive.

## Boot from USB Drive

1. Insert the bootable USB drive into the computer where you want to install Ubuntu.
2. Restart the computer.
3. Enter the BIOS or UEFI settings by pressing the appropriate key during startup (usually F2, F10, F12, or Del).
4. In the BIOS/UEFI settings, change the boot order to prioritize booting from the USB drive.
5. Save the changes and exit the BIOS/UEFI settings.
6. The computer will boot from the USB drive, and you'll see the Ubuntu installation screen.

## Install Ubuntu

1. Choose the language you want to use for the installation process and click "Install Ubuntu".
2. Select your keyboard layout and click "Continue".
3. Choose whether to install updates and third-party software during the installation and click "Continue".
4. Select the installation type:
    - **Normal Installation**: Install Ubuntu alongside an existing operating system or erase the disk and install Ubuntu.
    - **Advanced Partitioning**: Customize the disk partitions manually.
5. Follow the on-screen instructions to set your time zone, create a user account, and configure other settings.
6. Once the installation is complete, remove the USB drive and restart the computer.
7. Ubuntu should now be installed on your computer.

## Installing Visual Studio Code

1. Open the Terminal.
2. Run the following commands:
    ```bash
    sudo snap install --classic code
     ```

## Installing Python 3

1. Open the Terminal.
2. Run the following command:
    ```bash
    sudo apt update
    sudo apt install python3 python3-pip
    ```



## Making a Virtual Environment

1. Navigate to your project folder:
    ```bash
    cd my_project
    ```
2. Create a virtual environment named 'env' (you can replace 'env' with any name you prefer):
    ```bash
    python3 -m venv env
    ```

## Installing Requirements

1. Activate the virtual environment:
    ```bash
    source env/bin/activate
    ```
2. Assuming you have a `requirements.txt` file containing the required Python packages, install them using pip:
    ```bash
    pip install -r requirements.txt
    ```
3. Deactivate the virtual environment when you're done:
    ```bash
    deactivate
    ```


## Run 
1. After Activating the virtual environment run 
''' bash 
python3 app.py
'''