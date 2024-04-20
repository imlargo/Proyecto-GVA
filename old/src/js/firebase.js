import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.0/firebase-app.js";
import {
    getAuth, GoogleAuthProvider, signInWithPopup, signOut, onAuthStateChanged,
    setPersistence, browserLocalPersistence, browserSessionPersistence
} from "https://www.gstatic.com/firebasejs/10.7.0/firebase-auth.js";

import { getFirestore, collection, doc, addDoc, getDocs, setDoc, getDoc, deleteDoc } from "https://www.gstatic.com/firebasejs/10.7.0/firebase-firestore.js";

const firebaseConfig = {};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

// Auth
const auth = getAuth();
const provider = new GoogleAuthProvider()

const SignIn = () => signInWithPopup(auth, provider).then(
    (result) => console.log('User signed in:', result.user)
);
const SignOut = () => signOut(auth);

function addModal(SignIn) {
    const signInContainer = document.createElement("div");
    signInContainer.innerHTML = `
    <!-- Modal SignIn -->
    <div class="modal fade" id="modalSignIn" tabindex="-1" role="dialog" aria-labelledby="modalSignIn"
        aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLongTitle">Iniciar sesion</h5>
                </div>
                <div class="modal-body" id="bodyConfirmacion">
                    <p>Inicia sesion con google para poder llenar el formulario</p>
                    <button type="button" id="signInButton" class="login-with-google-btn">Iniciar sesion</button>
                </div>
                <div class="modal-footer">
                    <p>...</p>
                </div>
            </div>
        </div>
    </div>`;

    document.body.appendChild(signInContainer);
    const modal = new bootstrap.Modal(document.getElementById('modalSignIn'), {
        keyboard: false,
        backdrop: 'static'
    });
    const signInButton = document.getElementById("signInButton");
    signInButton.addEventListener('click', SignIn);
    return modal
}

const modal = addModal(SignIn);

setPersistence(auth, browserLocalPersistence).then(
    () => {
        onAuthStateChanged(auth, async (user) => {
            if (user) {
                // User is signed in.
                console.log('User is signed in:', user);

                const isValid = true;

                if (isValid) {
                    modal.hide();
                    GLOBALS.user = user;
                    firebaseCallback();
                } else {
                    SignOut(auth);
                    alert("No tienes permisos para acceder a esta aplicación.");
                }
            } else {
                // No user is signed in. Sign in.
                modal.show();
            }
        });
    });

// Base de datos
const db = getFirestore(app);
const coleccion = collection(db, "registros");
