from datetime import UTC, datetime, timedelta
from typing import Callable

import pytest
from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509 import CertificateBuilder, NameOID, random_serial_number


@pytest.fixture
def generate_certs() -> Callable[[str], tuple[str, str]]:
    def _generate_certs(cn: str) -> tuple[str, str]:
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

    return _generate_certs
