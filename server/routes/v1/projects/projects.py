from typing import List

from fastapi import status

from globals import caml_sdk
from routes.router import CAMLRouter
from schemas.project_schemas import ProjectCreateSchema, ProjectSchema

router = CAMLRouter(
    prefix="/projects",
    tags=["Projects"]
)


@router.post("", response_model=ProjectSchema, status_code=status.HTTP_201_CREATED)
async def create_project(project: ProjectCreateSchema):
    """
    Creates a new CAML project
    """

    project = caml_sdk.projects.create(project.name)
    return project.to_json()


@router.get("", response_model=List[ProjectSchema])
async def get_projects():
    """
    Returnes all CAML projects
    """
    projects = caml_sdk.projects.list()
    return [project.to_json() for project in projects]


@router.get("/{project_name}", response_model=ProjectSchema)
async def get_project(project_name: str):
    """
    Returns a CAML project by name
    """
    project = caml_sdk.projects.get(project_name)
    return project.to_json()


@router.delete("/{project_name}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_project(project_name: str):
    """
    Deletes a CAML project by name
    """
    caml_sdk.projects.delete(project_name)
