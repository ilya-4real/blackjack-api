from typing import Any, Dict, Optional

from fastapi.openapi.models import OAuthFlows, OAuthFlowPassword
from fastapi.security.oauth2 import OAuth2, OAuth2PasswordBearer
from fastapi import Request, HTTPException, status


class OAuthPasswordWithCookie(OAuth2):
    def __init__(
        self,
        tokenUrl: str,
        scheme_name: str | None = None,
        scopes: Optional[Dict[str, str]] = None,
        auto_error: bool = True,
    ):
        if not scopes:
            scopes = {}
        pass_flow = OAuthFlowPassword(tokenUrl=tokenUrl, scopes=scopes)
        flows = OAuthFlows(password=pass_flow)
        super().__init__(
            flows=flows,
            scheme_name=scheme_name,
            auto_error=auto_error,
        )

    def __call__(self, request: Request) -> Optional[str]:
        authorization: str | None = request.cookies.get("access_token")
        if not authorization:
            if self.auto_error:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="not authenticated",
                )
            else:
                return None
        return authorization
