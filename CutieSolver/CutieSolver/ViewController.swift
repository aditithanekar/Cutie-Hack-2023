//
//  ViewController.swift
//  CutieSolver
//
//  Created by Aditi Thanekar on 11/24/23.
//

import UIKit

class ViewController: UIViewController, UIImagePickerControllerDelegate, UINavigationControllerDelegate {

    private let takePhotoButton: UIButton = {
        let takePhotoButton = UIButton()
        takePhotoButton.backgroundColor = .white
        takePhotoButton.setTitle("Take a photo", for: .normal)
        takePhotoButton.setTitleColor(.black, for: .normal)
        return takePhotoButton
    }()
    private let chooseFromLibraryButton: UIButton = {
        let chooseFromLibraryButton = UIButton()
        chooseFromLibraryButton.backgroundColor = .white
        chooseFromLibraryButton.setTitle("Choose from library", for: .normal)
        chooseFromLibraryButton.setTitleColor(.black, for: .normal)
        return chooseFromLibraryButton
    }()
    private var imagePicker: UIImagePickerController = UIImagePickerController()


    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        view.backgroundColor = .systemMint
        view.addSubview(takePhotoButton)
        takePhotoButton.addTarget(self, action: #selector(addPhotoButtonPressed), for: .touchUpInside)
        view.addSubview(chooseFromLibraryButton)
        chooseFromLibraryButton.addTarget(self, action: #selector(selectPhotoFromLibraryPressed), for: .touchUpInside)
        
        
        ///
        // Set up image picker controller
        let imagePicker = UIImagePickerController()
        imagePicker.delegate = self
        imagePicker.allowsEditing = false // Set to true if you want to allow editing
        self.imagePicker=imagePicker // store it to the variable declared at the very top
                
        
    }
    override func viewDidLayoutSubviews() {
        super.viewDidLayoutSubviews()
        takePhotoButton.frame = CGRect(x: 20, y: view.frame.size.height-300, width: view.frame.size.width-50, height: 70)
        chooseFromLibraryButton.frame = CGRect(x: 20, y: view.frame.size.height-400, width: view.frame.size.width-50, height: 70)
        
    }
    

    @objc func addPhotoButtonPressed()
    {
        print("take photo click!")
        
    }
    @objc func selectPhotoFromLibraryPressed()
    {
        print("choose from library!")
        guard UIImagePickerController.isSourceTypeAvailable(.photoLibrary) else {
            // Photo library is not available
            return
        }
                
        // Set the source type to photo library
        imagePicker.sourceType = .photoLibrary
        present(imagePicker, animated: true, completion: nil)
        
        
    }
    func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [UIImagePickerController.InfoKey : Any]) {
        // Check if the selected media type is an image
        if let mediaType = info[.mediaType] as? String, mediaType == "public.image" {
            if let selectedImage = info[.originalImage] as? UIImage {
                // Handle the selected image here
                print("Selected image: \(selectedImage)")
                
                // Access other image information
                if let imageUrl = info[.imageURL] as? URL {
                    // Image URL: prints out the filepath of the image
                    print("Image URL: \(imageUrl)")
                }

            }
        }
        
        picker.dismiss(animated: true, completion: nil)
    }


}

