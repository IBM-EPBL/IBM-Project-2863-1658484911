{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "collapsed_sections": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "#Importing Keras libraries"
      ],
      "metadata": {
        "id": "5UKKDaCfUNCG"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import keras"
      ],
      "metadata": {
        "id": "ipCWLeFzUXGa"
      },
      "execution_count": 1,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Importing ImageDataGenerator from Keras"
      ],
      "metadata": {
        "id": "RNeZ0vrEUc55"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from matplotlib import pyplot as plt\n",
        "from keras.preprocessing.image import ImageDataGenerator"
      ],
      "metadata": {
        "id": "Mx2JxqSDUnPk"
      },
      "execution_count": 13,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Defining the Parameters"
      ],
      "metadata": {
        "id": "p7bB9Cd1b8kG"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "train_datagen=ImageDataGenerator(rescale=1./255,shear_range=0.2,rotation_range=180,zoom_range=0.2,horizontal_flip=True)\n",
        "test_datagen=ImageDataGenerator(rescale=1./255)\n"
      ],
      "metadata": {
        "id": "A1iR_1R-cKY4",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "88dcf3ab-3890-4436-9ef2-228d90919ccf"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<keras.preprocessing.image.ImageDataGenerator at 0x7fb7448ac110>"
            ]
          },
          "metadata": {},
          "execution_count": 11
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Applying ImageDataGenerator functionality to train dataset\n",
        "\n"
      ],
      "metadata": {
        "id": "pbYsUSI9rrd9"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jkgacY2Su-U1",
        "outputId": "5df3a800-71a1-4b1b-f2dc-b2dd14a773d7"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Drive already mounted at /content/drive; to attempt to forcibly remount, call drive.mount(\"/content/drive\", force_remount=True).\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x_train=train_datagen.flow_from_directory('/content/drive/MyDrive/IBM PROJECT/dataset/DATA SET/archive/Dataset/Dataset/train_set',target_size=(128,128),batch_size=32,class_mode='binary')\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3ou6I0e9sR7o",
        "outputId": "d7470cd8-5b7e-449e-d610-2698de4fce28"
      },
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Found 436 images belonging to 2 classes.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Applying ImageDataGenerator functionality to test dataset"
      ],
      "metadata": {
        "id": "943_QP5BtsLF"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "x_test=test_datagen.flow_from_directory('/content/drive/MyDrive/IBM PROJECT/dataset/DATA SET/archive/Dataset/Dataset/test_set',target_size=(128,128),batch_size=32,class_mode='binary')\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vIgeaeLht0Sn",
        "outputId": "6e70e72a-e047-448b-8da0-c80b3f995078"
      },
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Found 121 images belonging to 2 classes.\n"
          ]
        }
      ]
    }
  ]
}