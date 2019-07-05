import pendulum


def test_get_jobs_scheduled_jobs(job_store, job_factory):
    job_store.register_queue("foo")

    job_store.launch_job(
        job=job_factory(queue="foo", scheduled_at=pendulum.datetime(2000, 1, 1))
    )
    job_store.launch_job(
        job=job_factory(queue="foo", scheduled_at=pendulum.now().subtract(minutes=1))
    )
    job_store.launch_job(
        job=job_factory(queue="foo", scheduled_at=pendulum.datetime(2050, 1, 1))
    )

    jobs = list(job_store.get_jobs(queue="foo"))

    assert {job.id for job in jobs} == {0, 1}