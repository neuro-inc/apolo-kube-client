import base64
from datetime import UTC, datetime, timedelta

from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509 import CertificateBuilder, NameOID, random_serial_number


def escape_json_pointer(path: str) -> str:
    """
    Escapes ~ and / in a JSON Pointer path according to RFC 6901.
    Replaces ~ with ~0 and / with ~1.
    """
    return path.replace("~", "~0").replace("/", "~1")


def base64_encode(data: str) -> str:
    """Helper function to base64 encode a string."""
    return base64.b64encode(data.encode()).decode()


def base64_decode(data: str) -> str:
    """Helper function to base64 decode a string."""
    return base64.b64decode(data.encode()).decode()


def generate_certs(cn: str) -> tuple[str, str]:
    """
    Generates a self-signed certificate and private key for testing purposes.
    This function is a placeholder and does not perform any actual operations.
    """
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    pem_key = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    )

    # Generate self-signed certificate
    subject = issuer = x509.Name(
        [
            x509.NameAttribute(NameOID.COMMON_NAME, cn),
        ]
    )
    cert = (
        CertificateBuilder()
        .subject_name(subject)
        .issuer_name(issuer)
        .public_key(private_key.public_key())
        .serial_number(random_serial_number())
        .not_valid_before(datetime.now(UTC))
        .not_valid_after(datetime.now(UTC) + timedelta(days=365))
        .sign(private_key, algorithm=hashes.SHA256())
    )
    pem_cert = cert.public_bytes(serialization.Encoding.PEM)
    return pem_key.decode(), pem_cert.decode()
